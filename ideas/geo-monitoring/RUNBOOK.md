# Antigravity runbook — Stage 1 GEO monitoring

Комплект подготовлен поверх `7f8d88f` в ветке `validation/geo-stage1-kit`.
Он добавляет GEO-файлы, не меняя deck-результаты, общие skills или gates.
Это настройка исследования, не результаты валидации.

## 1. Получить комплект

Сначала останови пишущих агентов и проверь локальные изменения.
Если ветка уже опубликована в GitHub, используй:

```bash
git status --short
git fetch origin
git switch --track origin/validation/geo-stage1-kit
```

Последняя команда — только если локальной ветки ещё нет. Если она уже существует,
используй `git switch validation/geo-stage1-kit`. Если Git сообщает о конфликтующих
изменениях — остановись и сохрани/разбери их; не применяй reset, force checkout или
автоматический stash. Мердж в master для запуска не нужен.

Если комплект получен как patch, а удалённая ветка ещё не опубликована:

```bash
git status --short
git switch -c validation/geo-stage1-kit 7f8d88f
git am "C:/path/to/geo-stage1-kit.patch"
```

Замени путь к patch на фактический. Это вариант для новой локальной ветки и чистого
worktree; при уже существующей ветке не выполняй создание повторно. Patch содержит
один commit поверх `7f8d88f`. При ошибке применения остановись и разбери её; не
используй force или reset. После успешного применения можно опубликовать ветку
обычным `git push -u origin validation/geo-stage1-kit` со своими настроенными правами.

Открой корень существующего `saas-validation-starter`, а не `ideas/geo-monitoring`.
Используй установленный Python 3.10+; дополнительные пакеты не требуются.

## 2. Утвердить scope до исследования

Прочитай [hypothesis.yaml](hypothesis.yaml). Стартовое допущение:

- покупатель: владелец / руководитель SEO небольшого независимого SEO-агентства;
- организация: 2–20 сотрудников, recurring SMB engagements, отчёты на английском;
- задача: регулярное измерение AI-видимости и проверяемый клиентский отчёт;
- предполагаемое отличие: понятные изменения с сохранёнными основаниями и проверкой
  шума, связанные с реальным решением агентства;
- $100/месяц за agency account — бизнес-цель для проверки, не подтверждённый WTP;
- статьи, автопубликация, enterprise и direct-to-SMB продукт не входят в эту гипотезу.

Точные границы ICP — предложенный стартовый выбор, не факт из исследования. Запуск
первого research conversation означает, что ты принял эту версию для теста. Любые
изменения внеси и закоммить ДО запуска. После начала нельзя расширять ICP или снижать
gates, чтобы получить PASS. Новая гипотеза — новый явно зафиксированный проход.

## 3. Skills, безопасность и preflight

Используются существующие `.agent/skills` (именно единственное число `.agent`):
market-research, pain-mining, wtp-research, workflow-mapping, skeptic-research,
evidence-audit, stage1-judge. Убедись, что они доступны через `/` и правило
`.agent/rules/validation-rules.md` активно. Общие skills не нужно переписывать.

Запрети агенту доступ вне workspace и включи ручное подтверждение terminal commands.
Точные названия UI-переключателей могут отличаться в установленной версии;
ориентируйся на смысл разрешений, а не на обещание конкретного экрана.
Не включай blanket/always-allow для терминала. `/browser` означает разрешённую
браузерную функцию, а не разрешение читать профиль Chrome или кэш Antigravity.

Новый conversation без браузера: вставь блок из
`prompts/geo-monitoring/00-preflight.md`. Он проверит файлы и объяснит scope.
Единственная разрешённая ему команда:

```bash
python scripts/check_geo_stage1.py preflight
```

Preflight может пройти с пустыми output-директориями. Это НЕ означает, что evidence
собран или Stage 1 пройден. Отчёт настройки: `setup/preflight.md`.

## 4. Пять отдельных research conversations

Для экономии лимитов запускай последовательно или максимум по два одновременно.
Один writer на одну директорию; не смешивай разные conversation в одном raw/track.
Работай в одном checkout (Local Mode, если он так называется в твоей версии).
Во время запуска не переключай git-ветку. При отдельных worktrees сначала собери
готовые результаты в одну ветку; аудит нельзя делать по неполному набору worktrees.

| Conversation | Skill после `/browser` | Launch prompt | Reasoning | Пишет только |
| --- | --- | --- | --- | --- |
| A — Market | `/market-research` | `prompts/geo-monitoring/10-run-market.md` | Medium | `raw/market/` |
| B — Pain | `/pain-mining` | `prompts/geo-monitoring/11-run-pain.md` | High | `raw/pain/` |
| C — WTP | `/wtp-research` | `prompts/geo-monitoring/12-run-wtp.md` | High | `raw/wtp/` |
| D — Workflow | `/workflow-mapping` | `prompts/geo-monitoring/13-run-workflow.md` | Medium | `raw/workflow/` |
| E — Skeptic | `/skeptic-research` | `prompts/geo-monitoring/14-run-skeptic.md` | High | `raw/skeptic/` |

Это рекомендуемое распределение reasoning, не гарантия точности конкретной модели.
Используй доступную модель с работающим браузером; при лимите сохрани partial и
продолжи позже. Смена модели не заменяет проверку источников.

Вставляй текст из fenced-блока выбранного GEO prompt. Старые root-level prompts
ссылаются на deck-automation; не запускай их и не делай глобальную замену путей.
Каждый prompt уже включает свой полный путь и точную разрешённую команду.

Ориентир бюджета — до 45 минут discovery на track, остановка раньше при saturation.
Это ограничение работы, не требование ждать 45 минут. Evidence-цели не обязательны.
Каждый track сохраняет evidence.jsonl, отчёт и run-status.json. Raw всегда PENDING.

## 5. Если агент снова просит python -c или brain/cache

Отклони команду. Вставь:

> Stop this command. It is outside the GEO run's exact terminal allowlist. Do not
> use python -c, inline code, .gemini/antigravity/brain, generated steps or browser
> cache. Preserve the current authorized outputs and follow the checker command
> from the original GEO launch prompt. If blocked, record the blocker and end partial.

Не удаляй разговор или результаты для лечения петли. Останови активного writer;
продолжай по `prompts/geo-monitoring/90-resume.md` после восстановления инструмента.
Переоткрытый public source и внутренний content.md — не взаимозаменяемые источники.

## 6. Checkpoint перед Auditor

Когда все пять conversation закончены, из корня репозитория:

```bash
python scripts/check_geo_stage1.py raw-all
git status --short
```

Checker требует все пять outputs/статусов и проверяет каждую запись по текущей
канонической схеме, idea, ID prefixes и PENDING. Он выводит повторные URL/keys как
предупреждения для аудитора, а не автоматически удаляет их. Нулевое число записей
не означает failure скрипта, если пустой результат честно описан; gates не пройдут
на основании пустого результата. Исследовательские PARTIAL допускаются, ошибки
структуры — нет. Исправляет только владелец соответствующего raw/track.

После успешной проверки сохрани checkpoint только GEO-результатов:

```bash
git add ideas/geo-monitoring/raw
git diff --cached --name-status
git commit -m "Checkpoint GEO Stage 1 raw research"
```

Перед commit проверь, что в staging нет чужих ранее добавленных изменений.

## 7. Auditor, затем human spot-check

Новый conversation, High, `/browser` + `/evidence-audit`, prompt
`prompts/geo-monitoring/20-run-auditor.md`.

Auditor не ищет новые страницы и пишет только в `ideas/geo-monitoring/evidence/`.
Четыре результата: evidence.jsonl, audit-summary.md, high-impact-review.md,
scope-map.json. Sidecar показывает, какая запись относится к единственному ICP,
какие VERIFIED записи это подтверждают, и что осталось неизвестным.

```bash
python scripts/check_geo_stage1.py audit
```

Открой high-impact-review.md и проверь оригиналы сильнейших supporting/contradicting
записей, деньги, scope-linkage и substitutes. Особенно проверь: не перепутаны ли
цены с покупками, mentions с referrals, API с UI, функция конкурента с доказанным
«он уже всё решил». Неизвестное не исправляется догадкой.

Если нужен новый источник, верни конкретный вопрос ответственному researcher,
после его завершения повтори audit. Auditor сам не дополняет слабую базу.
Любое изменение raw после audit делает audit/scorecard устаревшими: повтори оба
последовательных шага. Не запускай Judge параллельно с исправлением evidence.

## 8. Judge

Новый conversation, High, **без `/browser`**, `/stage1-judge`, prompt
`prompts/geo-monitoring/30-run-judge.md`.

Результаты только `output/stage1-report.md` и `output/scorecard.json`.

```bash
python scripts/check_geo_stage1.py judge
```

Checker воспроизводит ID/counts, scope-ссылки, категории G3, числовые PASS thresholds
и базовую согласованность verdict. Семантика, достоверность и рыночный смысл остаются
за аудитом/человеком. FAIL нуждается в сильном опровержении; слабый dataset без него
даёт INSUFFICIENT EVIDENCE. CONDITIONAL PASS не маскирует несколько unknowns.

## 9. Сохранить и принести на независимый разбор

```bash
git add ideas/geo-monitoring
git diff --cached --name-status
git commit -m "Complete GEO Stage 1 research audit and judgment"
git push -u origin validation/geo-stage1-kit
```

Команда push не force. Если remote продвинулся или branch защищена — остановись,
не переписывай историю. После успешного push пришли commit SHA и четыре файла:
stage1-report.md, scorecard.json, evidence.jsonl, high-impact-review.md.
scope-map.json, audit-summary.md и raw остаются рядом для проверки.

Stage 1 PASS — разрешение рекомендовать interviews, не строить MVP. До независимого
разбора не запускай Stage 2, outreach или разработку; ChillPup не закрывается этим
исследованием. При непройденной GEO-гипотезе следующая в очереди — Multi-brand
content engine, а не автоматически другая версия GEO.
