import Link from "next/link";
import type { Article } from "@/utils/supabase/articles";

const dateFormatter = (lng: string) =>
  new Intl.DateTimeFormat(lng === "ja" ? "ja-JP" : "en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });

const ArticleCard: React.FC<{
  article: Article;
  lng: string;
  readMore?: string;
  rank?: number;
}> = ({ article, lng, rank }) => {
  return (
    <Link
      href={`/${lng}/${article.slug}`}
      className="flex flex-col gap-2 hover:opacity-80 transition-opacity"
    >
      <div className="relative w-full aspect-[16/9] rounded-xl bg-neutral-100 overflow-hidden">
        {article.image_url ? (
          // eslint-disable-next-line @next/next/no-img-element
          <img
            src={article.image_url}
            alt=""
            loading="lazy"
            referrerPolicy="no-referrer"
            className="w-full h-full object-cover"
          />
        ) : null}
        {rank !== undefined && (
          <span className="absolute top-2 left-2 flex items-center justify-center w-7 h-7 rounded-full bg-[#8771EF] text-white text-xs font-bold shadow">
            {rank}
          </span>
        )}
      </div>
      <span className="text-[11px] font-bold text-neutral-400">
        {dateFormatter(lng).format(new Date(article.published_at))}
      </span>
      <h2 className="text-sm sm:text-base font-bold text-black leading-snug line-clamp-3">
        {article.title}
      </h2>
    </Link>
  );
};

export default ArticleCard;
