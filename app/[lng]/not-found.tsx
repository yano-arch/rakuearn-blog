import Link from "next/link";

export default function NotFound() {
  return (
    <div className="min-h-[60vh] w-full flex flex-col items-center justify-center gap-4 px-6 text-center">
      <h1 className="text-2xl font-bold text-black">
        記事が見つかりませんでした
      </h1>
      <p className="text-neutral-500">
        お探しの記事は削除されたか、URLが間違っている可能性があります。
      </p>
      <Link href="/ja" className="text-[#8771EF] font-bold underline">
        トップへ戻る
      </Link>
    </div>
  );
}
