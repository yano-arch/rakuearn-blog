-- rakuearn blog: articles table
-- Run this once in the Supabase SQL editor (Project → SQL Editor → New query).

create table if not exists public.articles (
  id uuid primary key default gen_random_uuid(),
  slug text not null,
  lang text not null default 'ja',
  title text not null,
  excerpt text,
  content text not null,
  tags text[] default '{}',
  source_urls text[] default '{}',
  image_url text,
  image_credit text,
  image_credit_url text,
  view_count integer not null default 0,
  published boolean not null default true,
  published_at timestamptz not null default now(),
  created_at timestamptz not null default now(),
  unique (lang, slug)
);

create index if not exists articles_published_idx
  on public.articles (lang, published, published_at desc);

alter table public.articles enable row level security;

-- Anyone (the anon key used by the website) may read published articles only.
drop policy if exists "public can read published articles" on public.articles;
create policy "public can read published articles"
  on public.articles
  for select
  to anon
  using (published = true);

-- No insert/update/delete policy is defined for anon/authenticated:
-- writes are only possible with the service_role key (used by the
-- automated publishing pipeline), which bypasses RLS by design.

-- Lets the public website (using the anon key) safely increment an
-- article's view_count from the browser, without granting it general
-- UPDATE rights on the table (SECURITY DEFINER bypasses RLS just for
-- this one narrow operation).
create or replace function public.increment_view_count(article_slug text, article_lang text)
returns void
language sql
security definer
set search_path = public
as $$
  update public.articles
  set view_count = view_count + 1
  where slug = article_slug and lang = article_lang;
$$;

grant execute on function public.increment_view_count(text, text) to anon;
