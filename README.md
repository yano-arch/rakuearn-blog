# ミリオン記事速報

トレンドトピックを自動リサーチして記事化する、シンプルなNext.js + Supabaseのブログサイトです。

## セットアップ

### 1. 環境変数(Vercel)

Vercelのプロジェクト設定 → Environment Variables に以下を追加してください。

```
NEXT_PUBLIC_SUPABASE_URL=https://xxxxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
```

(この2つは公開しても問題ない値です。記事の閲覧のみに使われ、RLSにより公開記事しか読み取れません。)

### 2. Supabaseのテーブル作成

Supabaseダッシュボード → SQL Editor で `supabase/schema.sql` の内容を実行してください。`articles` テーブルとRLSポリシーが作成されます。

### 3. 記事の自動投稿(スケジュールタスク側)

以下の環境変数は **Vercelには設定しません**(公開してはいけない値のため)。記事自動生成を行うスケジュールタスク実行環境でのみ使用します。

```
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
```

- `scripts/list-recent-articles.js` : 直近の記事タイトル一覧を取得(重複テーマ回避用)
- `scripts/publish-article.js` : 記事1本をSupabaseに投稿

## ローカル開発

```bash
npm install
npm run dev
```

## 開発方針

- 会員登録・ログイン・ポイント交換・管理画面などポイ活関連の機能は全て削除し、記事の一覧・詳細のみのシンプルな構成にしています。
- 記事データはビルド時ではなくリクエスト時にSupabaseから取得しているため(`revalidate = 60`)、記事を追加してもサイトの再ビルドは不要です。
