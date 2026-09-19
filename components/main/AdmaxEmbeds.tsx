"use client";
import { useEffect } from "react";

// admax(忍者AdMax)の広告は、PC用とスマホ用で別々のスクリプトタグとして発行される。
// 記事側には空の枠(下記の各クラス名を付けたdiv)だけを置いておき、このコンポーネントが
// 実際の画面幅を見て、PC用/スマホ用どちらか一方の広告だけをiframe(srcdoc)として枠の中に
// 描画する。PC用スクリプトとスマホ用スクリプトの両方を同時に読み込むと二重にインプレッ
// ションが発生するため、必ずどちらか片方だけを選ぶ。
//
// 広告枠の種類(枠のclass名ごとに、挿入するadmax広告コードを切り替える):
// - admax-ad        : 「世間の反応」のツイート2件ごとに挟む広告
// - admax-ad-bottom : 記事本文(まとめ)の直後、記事の一番下に置く広告
const AD_SLOTS: Record<string, { pc: string; sp: string }> = {
  "admax-ad": {
    pc: "https://adm.shinobi.jp/s/a792318f347b5894d9ff7c73b4cab88a",
    sp: "https://adm.shinobi.jp/s/cf6dfc0a45b77b3b72d5ad46a6f656ad",
  },
  "admax-ad-bottom": {
    pc: "https://adm.shinobi.jp/s/423f8c90560b05dae474ac81d9eb2b5f",
    sp: "https://adm.shinobi.jp/s/fd7e616a909ecee5fb73c645753d40e5",
  },
};

// このサイトの他のレイアウト(max-sm:)と合わせ、640px未満をスマホ扱いとする。
const MOBILE_QUERY = "(max-width: 639px)";

function buildSrcDoc(adSrc: string) {
  return `<!DOCTYPE html><html><head><style>body{margin:0;padding:0;display:flex;justify-content:center;}</style></head><body><script src="${adSrc}"></script></body></html>`;
}

export default function AdmaxEmbeds() {
  useEffect(() => {
    const isMobile = window.matchMedia(MOBILE_QUERY).matches;

    Object.entries(AD_SLOTS).forEach(([className, { pc, sp }]) => {
      const adSrc = isMobile ? sp : pc;
      const slots = document.querySelectorAll<HTMLDivElement>(
        `.${className}:not([data-admax-loaded])`
      );

      slots.forEach((slot) => {
        slot.setAttribute("data-admax-loaded", "true");
        const iframe = document.createElement("iframe");
        iframe.scrolling = "no";
        iframe.setAttribute("frameborder", "0");
        iframe.style.cssText =
          "width:100%;max-width:336px;height:280px;border:0;display:block;margin:0 auto;";
        iframe.srcdoc = buildSrcDoc(adSrc);
        slot.appendChild(iframe);
      });
    });
  }, []);

  return null;
}
