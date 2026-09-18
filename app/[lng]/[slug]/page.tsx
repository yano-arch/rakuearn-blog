import { notFound } from "next/navigation";
import { marked } from "marked";
import Header from "@/components/layout/Header";
import Footer from "@/components/layout/Footer";
import { Layout } from "@/components/layout/Layout";
import { getArticleBySlug } from "@/utils/supabase/articles";
import { getT } from "@/app/i18n";

export const revalidate = 60;

const dateFormatter = (lng: string) =>
  new Intl.DateTimeFormat(lng === "ja" ? "ja-JP" : "en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });

export default async function ArticlePage({
  params,
}: {
  params: Promise<{ lng: string; slug: string }>;
}) {
  const { lng, slug } = await params;
  const { t: tHome } = await getT("home");
  const article = await getArticleBySlug(lng, slug);

  if (!article) {
    notFound();
  }

  const html = marked.parse(article.content, { async: false }) as string;

  return (
    <Layout>
      <div className="w-full max-w-[720px] px-6 max-sm:px-4">
        <Header />
        <article className="py-8">
          <p className="text-xs font-bold text-neutral-400 mb-3">
            {tHome("publishedOn")}:{" "}
            {dateFormatter(lng).format(new Date(article.published_at))}
          </p>
          <h1 className="text-3xl max-sm:text-2xl font-bold text-black leading-tight mb-6">
            {article.title}
          </h1>
          <div
            className="article-content"
            dangerouslySetInnerHTML={{ __html: html }}
          />
          {article.source_urls && article.source_urls.length > 0 && (
            <div className="mt-10 pt-6 border-t border-neutral-100">
              <p className="text-sm font-bold text-black mb-2">
                {tHome("sources")}
              </p>
              <ul className="list-disc pl-5 space-y-1">
                {article.source_urls.map((url) => (
                  <li key={url}>
                    <a
                      href={url}
                      target="_blank"
                      rel="noopener noreferrer nofollow"
                      className="text-sm text-[#8771EF] break-all"
                    >
                      {url}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </article>
        <Footer />
      </div>
    </Layout>
  );
}
