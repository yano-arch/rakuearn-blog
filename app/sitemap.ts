import type { MetadataRoute } from "next";
import { languages } from "@/app/i18n/settings";
import { getArticles } from "@/utils/supabase/articles";

const SITE_URL = "https://rakuearn-blog.vercel.app";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const entries: MetadataRoute.Sitemap = [];

  for (const lng of languages) {
    entries.push({
      url: `${SITE_URL}/${lng}`,
      changeFrequency: "hourly",
      priority: 1,
    });
    entries.push({
      url: `${SITE_URL}/${lng}/ranking`,
      changeFrequency: "hourly",
      priority: 0.6,
    });

    const articles = await getArticles(lng);
    for (const article of articles) {
      entries.push({
        url: `${SITE_URL}/${lng}/${article.slug}`,
        lastModified: new Date(article.published_at),
        changeFrequency: "daily",
        priority: 0.8,
      });
    }
  }

  return entries;
}
