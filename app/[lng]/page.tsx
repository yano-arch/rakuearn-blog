import Link from "next/link";
import Header from "@/components/layout/Header";
import Footer from "@/components/layout/Footer";
import { Layout } from "@/components/layout/Layout";
import ArticleCard from "@/components/main/ArticleCard";
import { getArticles } from "@/utils/supabase/articles";
import { getT } from "@/app/i18n";
import { languages } from "@/app/i18n/settings";

export async function generateStaticParams() {
  return languages.map((lng) => ({ lng }));
}

export const revalidate = 60;

const dateFormatter = (lng: string) =>
  new Intl.DateTimeFormat(lng === "ja" ? "ja-JP" : "en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });

export default async function HomePage({
  params,
}: {
  params: Promise<{ lng: string }>;
}) {
  const { lng } = await params;
  const { t: tHome } = await getT("home");
  const { t: tCommon } = await getT("common");
  const articles = await getArticles(lng);
  const featured = articles.find((a) => a.image_url) ?? null;
  const restArticles = featured
    ? articles.filter((a) => a.id !== featured.id)
    : articles;

  return (
    <Layout>
      <div className="w-full max-w-[720px] px-6 max-sm:px-4">
        <Header />
        <section className="py-10 max-sm:py-6 border-b border-neutral-100">
          <p className="text-sm font-bold text-[#8771EF] mb-3">
            {tCommon("tagline")}
          </p>
          <h1 className="text-3xl max-sm:text-2xl font-bold text-black leading-tight mb-4">
            {tHome("heroTitle")}
          </h1>
          <p className="text-base text-neutral-600 leading-relaxed">
            {tHome("heroSubtitle")}
          </p>
        </section>
        {featured && (
          <section className="py-8 border-b border-neutral-100">
            <Link href={`/${lng}/${featured.slug}`} className="block group">
              <figure className="mb-4">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img
                  src={featured.image_url!}
                  alt=""
                  referrerPolicy="no-referrer"
                  className="w-full aspect-[16/9] object-cover rounded-2xl bg-neutral-100 group-hover:opacity-90 transition-opacity"
                />
                {featured.image_credit && (
                  <figcaption className="mt-2 text-xs text-neutral-400">
                    {featured.image_credit}
                  </figcaption>
                )}
              </figure>
              <span className="text-xs font-bold text-neutral-400">
                {dateFormatter(lng).format(new Date(featured.published_at))}
              </span>
              <h2 className="text-2xl max-sm:text-xl font-bold text-black leading-snug mt-1 mb-2 group-hover:text-[#8771EF] transition-colors">
                {featured.title}
              </h2>
              {featured.excerpt && (
                <p className="text-base text-neutral-600 leading-relaxed">
                  {featured.excerpt}
                </p>
              )}
            </Link>
          </section>
        )}
        <section className="py-8">
          <h2 className="text-lg font-bold text-black mb-2">
            {tHome("latestArticles")}
          </h2>
          {restArticles.length === 0 ? (
            <p className="py-10 text-neutral-500">{tHome("noArticles")}</p>
          ) : (
            <div className="grid grid-cols-2 gap-x-4 gap-y-8 sm:gap-x-6">
              {restArticles.map((article) => (
                <ArticleCard key={article.id} article={article} lng={lng} />
              ))}
            </div>
          )}
        </section>
        <Footer />
      </div>
    </Layout>
  );
}
