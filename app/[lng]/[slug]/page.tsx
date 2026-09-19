import { notFound } from "next/navigation";
import { marked } from "marked";
import type { Metadata } from "next";
import Header from "@/components/layout/Header";
import Footer from "@/components/layout/Footer";
import { Layout } from "@/components/layout/Layout";
import ViewTracker from "@/components/main/ViewTracker";
import TweetEmbeds from "@/components/main/TweetEmbeds";
import { getArticleBySlug } from "@/utils/supabase/articles";
import { getT } from "@/app/i18n";

export const revalidate = 60;

const SITE_URL = "https://rakuearn-blog.vercel.app";
const SITE_NAME = "ミリオン記事速報";

const dateFormatter = (lng: string) =>
  new Intl.DateTimeFormat(lng === "ja" ? "ja-JP" : "en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });

export async function generateMetadata({
  params,
}: {
  params: Promise<{ lng: string; slug: string }>;
}): Promise<Metadata> {
  const { lng, slug } = await params;
  const article = await getArticleBySlug(lng, slug);

  if (!article) {
    return { title: "記事が見つかりませんでした" };
  }

  const url = `${SITE_URL}/${lng}/${slug}`;
  const description =
    article.excerpt ?? article.title.slice(0, 120);

  return {
    // The root layout's title.template appends " | サイト名" automatically,
    // so this stays just the article title to avoid the site name showing twice.
    title: article.title,
    description,
    alternates: { canonical: url },
    openGraph: {
      title: article.title,
      description,
      url,
      siteName: SITE_NAME,
      type: "article",
      publishedTime: article.published_at,
      locale: lng === "ja" ? "ja_JP" : "en_US",
      images: article.image_url
        ? [{ url: article.image_url, width: 1600, height: 900 }]
        : undefined,
    },
    twitter: {
      card: "summary_large_image",
      title: article.title,
      description,
      images: article.image_url ? [article.image_url] : undefined,
    },
  };
}

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

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "NewsArticle",
    headline: article.title,
    description: article.excerpt ?? undefined,
    image: article.image_url ? [article.image_url] : undefined,
    datePublished: article.published_at,
    dateModified: article.published_at,
    inLanguage: lng,
    author: [{ "@type": "Organization", name: SITE_NAME }],
    publisher: {
      "@type": "Organization",
      name: SITE_NAME,
      logo: {
        "@type": "ImageObject",
        url: `${SITE_URL}/${lng}/favicon.ico`,
      },
    },
    mainEntityOfPage: {
      "@type": "WebPage",
      "@id": `${SITE_URL}/${lng}/${article.slug}`,
    },
  };

  return (
    <Layout>
      <div className="w-full max-w-[720px] px-6 max-sm:px-4">
        <script
          type="application/ld+json"
          // eslint-disable-next-line react/no-danger
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
        <Header />
        <ViewTracker slug={article.slug} lang={lng} />
        <TweetEmbeds />
        <article className="py-8">
          <p className="text-xs font-bold text-neutral-400 mb-3 flex flex-wrap items-center gap-x-3 gap-y-1">
            <span>
              {tHome("publishedOn")}:{" "}
              {dateFormatter(lng).format(new Date(article.published_at))}
            </span>
            <span className="inline-flex items-center gap-1">
              <svg
                width="14"
                height="14"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                aria-hidden="true"
              >
                <path d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7-11-7-11-7z" />
                <circle cx="12" cy="12" r="3" />
              </svg>
              {tHome("views")}: {(article.view_count ?? 0).toLocaleString(lng === "ja" ? "ja-JP" : "en-US")}
            </span>
          </p>
          <h1 className="text-3xl max-sm:text-2xl font-bold text-black leading-tight mb-6">
            {article.title}
          </h1>
          {article.image_url && (
            <figure className="mb-6">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={article.image_url}
                alt=""
                referrerPolicy="no-referrer"
                className="w-full rounded-xl bg-neutral-100"
              />
              {article.image_credit && (
                <figcaption className="mt-2 text-xs text-neutral-400">
                  {article.image_credit_url ? (
                    <a
                      href={article.image_credit_url}
                      target="_blank"
                      rel="noopener noreferrer nofollow"
                      className="hover:text-neutral-600"
                    >
                      {article.image_credit}
                    </a>
                  ) : (
                    article.image_credit
                  )}
                </figcaption>
              )}
            </figure>
          )}
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
