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

export default async function HomePage({
  params,
}: {
  params: Promise<{ lng: string }>;
}) {
  const { lng } = await params;
  const { t: tHome } = await getT("home");
  const { t: tCommon } = await getT("common");
  const articles = await getArticles(lng);

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
        <section className="py-8">
          <h2 className="text-lg font-bold text-black mb-2">
            {tHome("latestArticles")}
          </h2>
          {articles.length === 0 ? (
            <p className="py-10 text-neutral-500">{tHome("noArticles")}</p>
          ) : (
            <div className="flex flex-col">
              {articles.map((article) => (
                <ArticleCard
                  key={article.id}
                  article={article}
                  lng={lng}
                  readMore={tHome("readMore")}
                />
              ))}
            </div>
          )}
        </section>
        <Footer />
      </div>
    </Layout>
  );
}
