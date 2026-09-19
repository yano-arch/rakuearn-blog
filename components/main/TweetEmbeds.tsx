"use client";
import { useEffect } from "react";

declare global {
  interface Window {
    twttr?: {
      widgets: {
        load: (el?: HTMLElement) => void;
      };
    };
  }
}

// Article bodies can contain raw <blockquote class="twitter-tweet"> markup
// (embedded by the article-writing automation to show real public reaction
// posts). This loads Twitter/X's widgets.js once and asks it to scan the
// page and turn those blockquotes into the real rendered tweet embeds.
export default function TweetEmbeds() {
  useEffect(() => {
    const loadWidgets = () => window.twttr?.widgets?.load();

    if (window.twttr) {
      loadWidgets();
      return;
    }

    const existing = document.querySelector<HTMLScriptElement>(
      'script[src="https://platform.twitter.com/widgets.js"]'
    );
    if (existing) {
      existing.addEventListener("load", loadWidgets);
      return () => existing.removeEventListener("load", loadWidgets);
    }

    const script = document.createElement("script");
    script.src = "https://platform.twitter.com/widgets.js";
    script.async = true;
    script.charset = "utf-8";
    script.addEventListener("load", loadWidgets);
    document.body.appendChild(script);
  }, []);

  return null;
}
