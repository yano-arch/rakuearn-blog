"use client";
import { useEffect } from "react";
import { createClient } from "@supabase/supabase-js";

// Fires once per page view (client-side) to increment the article's
// view_count via a Postgres RPC function, so it works correctly even
// though the page itself is served from an ISR cache.
export default function ViewTracker({
  slug,
  lang,
}: {
  slug: string;
  lang: string;
}) {
  useEffect(() => {
    const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
    const anonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
    if (!url || !anonKey) return;
    const supabase = createClient(url, anonKey, {
      auth: { persistSession: false },
    });
    supabase
      .rpc("increment_view_count", { article_slug: slug, article_lang: lang })
      .then(({ error }) => {
        if (error) console.error("Failed to record view", error.message);
      });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [slug, lang]);

  return null;
}
