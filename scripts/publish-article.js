#!/usr/bin/env node
/**
 * Insert one article into Supabase.
 *
 * Usage:
 *   SUPABASE_URL=... SUPABASE_SERVICE_ROLE_KEY=... node scripts/publish-article.js article.json
 *
 * article.json shape:
 *   {
 *     "slug": "kebab-case-slug",
 *     "lang": "ja",
 *     "title": "...",
 *     "excerpt": "...",
 *     "content": "markdown body...",
 *     "tags": ["tag1", "tag2"],
 *     "source_urls": ["https://..."]
 *   }
 */

const fs = require("fs");

async function main() {
  const filePath = process.argv[2];
  if (!filePath) {
    console.error("Usage: node scripts/publish-article.js <article.json>");
    process.exit(1);
  }

  const supabaseUrl = process.env.SUPABASE_URL;
  const serviceRoleKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!supabaseUrl || !serviceRoleKey) {
    console.error(
      "Missing SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY environment variables."
    );
    process.exit(1);
  }

  const raw = fs.readFileSync(filePath, "utf-8");
  const article = JSON.parse(raw);

  const required = ["slug", "title", "content"];
  for (const key of required) {
    if (!article[key]) {
      console.error(`article.json is missing required field: ${key}`);
      process.exit(1);
    }
  }
  article.lang = article.lang || "ja";
  article.tags = article.tags || [];
  article.source_urls = article.source_urls || [];
  article.published = true;
  article.published_at = article.published_at || new Date().toISOString();

  const res = await fetch(`${supabaseUrl}/rest/v1/articles`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      apikey: serviceRoleKey,
      Authorization: `Bearer ${serviceRoleKey}`,
      Prefer: "return=representation",
    },
    body: JSON.stringify(article),
  });

  const text = await res.text();
  if (!res.ok) {
    console.error(`Supabase insert failed (${res.status}): ${text}`);
    process.exit(1);
  }

  console.log("Published:", text);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
