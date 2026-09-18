import { createClient } from "@supabase/supabase-js";

export type Article = {
  id: string;
  slug: string;
  title: string;
  excerpt: string | null;
  content: string;
  lang: string;
  tags: string[] | null;
  source_urls: string[] | null;
  published: boolean;
  published_at: string;
  created_at: string;
};

// Read-only client using the public anon key. Only rows allowed by the
// `articles` table's RLS policy (published = true) are ever returned.
function getSupabase() {
  const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const anonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
  if (!url || !anonKey) return null;
  return createClient(url, anonKey, {
    auth: { persistSession: false },
  });
}

export async function getArticles(lang: string): Promise<Article[]> {
  const supabase = getSupabase();
  if (!supabase) return [];
  const { data, error } = await supabase
    .from("articles")
    .select("*")
    .eq("published", true)
    .eq("lang", lang)
    .order("published_at", { ascending: false });
  if (error) {
    console.error("Failed to load articles", error.message);
    return [];
  }
  return data ?? [];
}

export async function getArticleBySlug(
  lang: string,
  slug: string
): Promise<Article | null> {
  const supabase = getSupabase();
  if (!supabase) return null;
  const { data, error } = await supabase
    .from("articles")
    .select("*")
    .eq("published", true)
    .eq("lang", lang)
    .eq("slug", slug)
    .maybeSingle();
  if (error) {
    console.error("Failed to load article", error.message);
    return null;
  }
  return data;
}
