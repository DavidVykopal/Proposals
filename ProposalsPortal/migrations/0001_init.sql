CREATE TABLE comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  doc TEXT NOT NULL,
  anchor TEXT NOT NULL,
  quote TEXT,
  parent_id INTEGER REFERENCES comments(id),
  author TEXT NOT NULL,
  body TEXT NOT NULL,
  resolved INTEGER NOT NULL DEFAULT 0,
  resolved_by TEXT,
  resolved_at TEXT,
  edited_at TEXT,
  deleted INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX idx_comments_doc ON comments(doc, deleted);
CREATE INDEX idx_comments_parent ON comments(parent_id);

CREATE TABLE views (
  viewer TEXT NOT NULL,
  doc TEXT NOT NULL,
  first_at TEXT NOT NULL DEFAULT (datetime('now')),
  last_at TEXT NOT NULL DEFAULT (datetime('now')),
  count INTEGER NOT NULL DEFAULT 1,
  PRIMARY KEY (viewer, doc)
);
