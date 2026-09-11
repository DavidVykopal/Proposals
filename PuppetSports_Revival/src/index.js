/**
 * Language routing for the Puppet Sports Revival proposal site.
 *
 * English is the default and always the fallback. A visitor gets a translated
 * page when we have one AND one of these says so, in order of priority:
 *
 *   1. an explicit choice        ?lang=cs  ?lang=en  ?cs  ?en   (also stored in a cookie)
 *   2. a previous explicit choice (cookie)
 *   3. the connecting country    request.cf.country === 'CZ'
 *   4. Accept-Language
 *
 * An explicit choice always wins over geography, so a Czech visitor who asks for
 * English is not dragged back to Czech on the next click.
 *
 * To add a language: add its code to LANGS and ship <page>.<code>.html files.
 * Anything without a translated file silently falls back to English.
 */

const DEFAULT_LANG = "en";
const LANGS = ["en", "cs"];

// Which connecting countries imply which language.
const COUNTRY_LANG = { CZ: "cs" };

// Pages that exist in translation. Everything else is served as-is.
const PAGES = new Set(["index", "soccer", "hockey"]);

const COOKIE = "psr_lang";
const YEAR = 60 * 60 * 24 * 365;

function pickExplicit(url) {
  const q = url.searchParams;
  const named = (q.get("lang") || q.get("hl") || "").toLowerCase();
  if (LANGS.includes(named)) return named;
  // bare flag form, e.g. /?cs
  for (const code of LANGS) if (q.has(code)) return code;
  return null;
}

function fromCookie(request) {
  const header = request.headers.get("Cookie") || "";
  const hit = header.match(new RegExp("(?:^|;\\s*)" + COOKIE + "=([a-z-]+)"));
  return hit && LANGS.includes(hit[1]) ? hit[1] : null;
}

function fromAcceptLanguage(request) {
  const header = request.headers.get("Accept-Language") || "";
  for (const part of header.split(",")) {
    const tag = part.split(";")[0].trim().toLowerCase();
    if (!tag) continue;
    const base = tag.split("-")[0];
    if (LANGS.includes(base)) return base;
  }
  return null;
}

/** Resolve "/soccer", "/soccer.html" and "/" to a page name. */
function pageName(pathname) {
  let p = pathname.replace(/\/+$/, "");
  if (p === "" || p === "/index") return "index";
  p = p.replace(/^\//, "").replace(/\.html$/, "");
  return p;
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // One canonical host: www redirects to the apex, query string preserved.
    if (url.hostname === "www.puppetsports.com") {
      url.hostname = "puppetsports.com";
      return Response.redirect(url.toString(), 301);
    }

    // Assets and anything with a file extension go straight through.
    if (url.pathname.startsWith("/assets/") || /\.[a-z0-9]+$/i.test(url.pathname.replace(/\.html$/, ""))) {
      return env.ASSETS.fetch(request);
    }

    const page = pageName(url.pathname);
    const explicit = pickExplicit(url);

    const lang =
      explicit ||
      fromCookie(request) ||
      COUNTRY_LANG[(request.cf && request.cf.country) || request.headers.get("CF-IPCountry")] ||
      fromAcceptLanguage(request) ||
      DEFAULT_LANG;

    let response;
    let served = DEFAULT_LANG;

    if (lang !== DEFAULT_LANG && PAGES.has(page)) {
      const variant = new URL(`/${page}.${lang}.html`, url.origin);
      const candidate = await env.ASSETS.fetch(new Request(variant, request));
      if (candidate.status === 200) {
        response = candidate;
        served = lang;
      }
    }

    if (!response) {
      const canonical = new URL(page === "index" ? "/index.html" : `/${page}.html`, url.origin);
      response = await env.ASSETS.fetch(new Request(canonical, request));
    }

    response = new Response(response.body, response);
    response.headers.set("Content-Language", served);
    // Be explicit about UTF-8 so Czech diacritics never depend on browser guessing.
    const type = response.headers.get("Content-Type") || "";
    if (type.startsWith("text/html") && !/charset/i.test(type)) {
      response.headers.set("Content-Type", "text/html; charset=utf-8");
    }
    // The same URL can return either language, so it must not be shared-cached.
    response.headers.set("Cache-Control", "no-store");
    response.headers.append("Vary", "Cookie, Accept-Language, CF-IPCountry");

    // Remember an explicit choice so it survives the next click.
    if (explicit) {
      response.headers.append(
        "Set-Cookie",
        `${COOKIE}=${explicit}; Path=/; Max-Age=${YEAR}; SameSite=Lax; Secure`
      );
    }

    return response;
  },
};
