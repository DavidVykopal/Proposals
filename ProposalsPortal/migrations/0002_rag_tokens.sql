CREATE TABLE docs (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  section TEXT NOT NULL,
  section_title TEXT NOT NULL,
  route TEXT NOT NULL,
  kind TEXT NOT NULL,
  modified TEXT,
  summary TEXT,
  text TEXT NOT NULL
);

CREATE VIRTUAL TABLE chunks USING fts5(
  doc UNINDEXED,
  anchor UNINDEXED,
  heading,
  text,
  tokenize = 'unicode61 remove_diacritics 2'
);

CREATE TABLE tokens (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  owner TEXT NOT NULL,
  label TEXT,
  prefix TEXT NOT NULL,
  token_hash TEXT NOT NULL UNIQUE,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  last_used_at TEXT,
  revoked INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE chat_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  who TEXT NOT NULL,
  scope TEXT,
  question TEXT NOT NULL,
  answer TEXT,
  tools TEXT,
  model TEXT,
  tokens_in INTEGER,
  tokens_out INTEGER,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
