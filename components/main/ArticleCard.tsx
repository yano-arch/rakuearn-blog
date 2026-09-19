import Link from "next/link";
import type { Article } from "@/utils/supabase/articles";

const dateFormatter = (lng: string) =>
  new Intl.DateTimeFormat(lng === "ja" ? "ja-JP" : "en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });

const ArticleCard: React.FC<{ article: Article; lng: string; readMore: string }> = ({
  article,
  lng,
  readMore,
}) => {
  return (
    <Link
      href={`/${lng}/${article.slug}`}
      className="flex flex-col gap-3 py-6 border-b border-neutral-100 hover:opacity-70 transition-opacity"
    >
      {article.image_url && (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          src={article.image_url}
          alt=""
          loading="lazy"
          referrerPolicy="no-referrer"
          className="w-full aspect-[16/9] object-cover rounded-xl bg-neutral-100"
        />
      )}
      <span className="text-xs font-bold text-neutral-400">
        {dateFormatter(lng).format(new Date(article.published_at))}
      </span>
      <h2 className="text-xl font-bold text-black leading-snug">{article.title}</h2>
      {article.excerpt && (
        <p className="text-sm text-neutral-600 leading-relaxed">{article.excerpt}</p>
      )}
      {article.tags && article.tags.length > 0 && (
        <div className="flex flex-wrap gap-2">
          {article.tags.map((tag) => (
            <span
              key={tag}
              className="text-xs font-bold text-[#8771EF] bg-[#F6F5F9] rounded-full px-3 py-1"
            >
              #{tag}
            </span>
          ))}
        </div>
      )}
      <span className="text-sm font-bold text-[#8771EF]">{readMore} →</span>
    </Link>
  );
};

export default ArticleCard;
