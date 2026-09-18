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
