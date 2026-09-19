"use client";
import { useEffect } from "react";

// admax(忍者AdMax)の広告は、PC用とスマホ用で別々のスクリプトタグとして発行される。
// 記事本文(Markdown)側には <div class="admax-ad"></div> という空の枠だけを置いておき、
// このコンポーネントが実際の画面幅を見て、PC用/スマホ用どちらか一方の広告だけを
// iframe(srcdoc)として枠の中に描画する。PC用スクリプトとスマホ用スクリプトの両方を
// 同時に読み込んでしまうと二重にインプレッションが発生するため、必ずどちらか片方だけを選ぶ。
const PC_AD_SRC = "https://adm.shinobi.jp/s/a792318f347b5894d9ff7c73b4cab88a";
const SP_AD_SRC = "https://adm.shinobi.jp/s/cf6dfc0a45b77b3b72d5ad46a6f656ad";

// このサイトの他のレイアウト(max-sm:)と合わせ、640px未満をスマホ扱いとする。
const MOBILE_QUERY = "(max-width: 639px)";

function buildSrcDoc(adSrc: string) {
  return `<!DOCTYPE html><html><head><style>body{margin:0;padding:0;display:flex;justify-content:center;}</style></head><body><script src="${adSrc}"></script></body></html>`;
}

export default function AdmaxEmbeds() {
  useEffect(() => {
    const isMobile = window.matchMedia(MOBILE_QUERY).matches;
    const adSrc = isMobile ? SP_AD_SRC : PC_AD_SRC;

    const slots = document.querySelectorAll<HTMLDivElement>(
      ".admax-ad:not([data-admax-loaded])"
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
  }, []);

  return null;
}
