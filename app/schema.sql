create table if not exists sources (
id serial primary key,
code text unique not null, -- 'HKPF','HKMA','SFC' 等
name text not null
);


create table if not exists numbers (
id bigserial primary key,
e164 text not null unique, -- 標準化電話（+852...）
is_overseas boolean default false
);


create table if not exists number_labels (
id bigserial primary key,
number_id bigint not null references numbers(id) on delete cascade,
label text not null, -- scam / telemarketing / robocall / finance_risk
confidence smallint not null default 50,
first_seen timestamptz not null default now(),
last_seen timestamptz not null default now()
);


create table if not exists number_evidence (
id bigserial primary key,
number_id bigint not null references numbers(id) on delete cascade,
source_id int not null references sources(id),
url text,
snippet text,
created_at timestamptz not null default now()
);


create table if not exists risk_scores (
number_id bigint primary key references numbers(id) on delete cascade,
score smallint not null default 0, -- 0-100
decision text not null default 'warn', -- block/warn/allow
updated_at timestamptz not null default now()
);


create table if not exists deltas (
id bigserial primary key,
kind text not null, -- 'add' | 'remove'
e164 text not null,
payload jsonb not null,
created_at timestamptz not null default now()
);


insert into sources(code,name) values
('HKPF','Hong Kong Police Force'),
('HKMA','Hong Kong Monetary Authority'),
('SFC','Securities and Futures Commission')
on conflict (code) do nothing;

