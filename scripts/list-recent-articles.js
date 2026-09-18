#!/usr/bin/env node
/**
 * List recently published articles (title + tags + date), so the article
 * generation pipeline can avoid writing about the same topic twice.
 *
 * Usage:
 *   SUPABASE_URL=... SUPABASE_SERVICE_ROLE_KEY=... node scripts/list-recent-articles.js [days]
 */

async function main() {
  const days = Number(process.argv[2] || 14);
  const supabaseUrl = process.env.SUPABASE_URL;
  const serviceRoleKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!supabaseUrl || !serviceRoleKey) {
    console.error(
      "Missing SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY environment variables."
    );
    process.exit(1);
  }

  const since = new Date(Date.now() - days * 24 * 60 * 60 * 1000).toISOString();
  const url = `${supabaseUrl}/rest/v1/articles?select=title,slug,tags,published_at&published_at=gte.${encodeURIComponent(
    since
  )}&order=published_at.desc`;

  const res = await fetch(url, {
    headers: {
      apikey: serviceRoleKey,
      Authorization: `Bearer ${serviceRoleKey}`,
    },
  });

  const text = await res.text();
  if (!res.ok) {
    console.error(`Supabase query failed (${res.status}): ${text}`);
    process.exit(1);
  }

  console.log(text);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
