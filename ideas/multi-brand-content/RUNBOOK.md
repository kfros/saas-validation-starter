# Antigravity runbook — Multi-brand content, Stage 1

Комплект подготовлен поверх `fb23781` (завершённый GEO Stage 1).
Рабочая ветка: `validation/multi-brand-stage1-kit`.
Это инструкции для нового исследования, а не результаты валидации.

## 1. Установить комплект

Останови агентов, которые сейчас записывают файлы в репозиторий. Проверь:

```bash
git status --short
git fetch origin
```

Далее выбери один способ получения комплекта.

**Если получен patch**, из чистого worktree существующего репозитория:

```bash
git switch -c validation/multi-brand-stage1-kit fb23781
git am "C:/path/to/multi-brand-stage1-kit.patch"
```

Замени путь к patch на фактический. Patch содержит один добавочный commit поверх
`fb23781`; он включает только Multi-brand ideas/prompts и свой checker с тестами.

**Если ветка уже опубликована**, а локальной ветки ещё нет:

```bash
git switch --track origin/validation/multi-brand-stage1-kit
```

При существующей локальной ветке используй `git switch validation/multi-brand-stage1-kit`.
Не применяй patch второй раз. Мердж в master для запуска не нужен.

Если есть незакоммиченные изменения, незавершённый git am или конфликт при применении,
сначала сохрани и разбери их. Не используй reset/force checkout/автоматический stash.
Не создавай ветку повторно, если она уже существует.

## 2. Открыть проект и прочитать scope

Открой **корень saas-validation-starter**, не вложенную папку идеи.
Skills остаются в `.agent/skills` — `.agent` в единственном числе.

Прочитай [hypothesis.yaml](hypothesis.yaml) и [research-brief.md](research-brief.md).

Проверяем владельца SMM-практики/небольшого агентства, который сам участвует
в производстве или существенных правках статического контента для нескольких
независимых SMB-клиентов и выбирает инструменты. Результат — посты/карусели
с подписями, готовые к проверке, правкам и передаче в существующий publishing workflow.

Это рабочая гипотеза. Цену пока не задаём. Учитываем фрилансеров и агентства,
но агент должен отдельно показать их workflow и покупки. Точного ограничения
по headcount нет; придумывать размер команды или количество клиентов нельзя.

Отдельные боли автопостинга, аналитики, рекламы и видеопроизводства не подтверждают
этот scope. Если сознательно меняешь buyer/job до запуска, сначала нужно согласовать
hypothesis/brief/protocol/prompts/checker; не правь их по ходу исследования ради PASS.
Обычный запуск данного комплекта уже выбирает записанную гипотезу для проверки.

## 3. Проверить среду

Нужен установленный Python 3.10+; дополнительных пакетов нет.
Команды ниже запускаются человеком из корня репозитория:

```bash
python scripts/check_multibrand_stage1.py preflight
python -m unittest discover -s scripts -p test_check_multibrand_stage1.py
```

Если `python` отсутствует, сначала настрой интерпретатор в своей среде. Не поручай
research-агенту устанавливать пакеты или подбирать терминальные обходы.

Затем новый conversation: prompt
`prompts/multi-brand-content/00-preflight.md`, без browser.
Результат: `ideas/multi-brand-content/setup/preflight.md`.
Если skills не видны или есть конфликт инструкций, устрани конкретный blocker
до исследования. Повторная формальная просьба «утвердить гипотезу» не нужна.

## 4. Пять отдельных research conversations

В каждой включи `/browser`, нужный skill и вставь **текст из fenced-блока**
соответствующего prompt. Не запускай старые root-level deck или GEO prompts.

| Порядок | Skill | Prompt | Рекомендуемое reasoning |
| --- | --- | --- | --- |
| A — Market | `/market-research` | `10-run-market.md` | Medium |
| B — Pain | `/pain-mining` | `11-run-pain.md` | High |
| C — WTP | `/wtp-research` | `12-run-wtp.md` | High |
| D — Workflow | `/workflow-mapping` | `13-run-workflow.md` | Medium |
| E — Skeptic | `/skeptic-research` | `14-run-skeptic.md` | High |

Все пути относятся к `prompts/multi-brand-content/`.
Это рекомендации по распределению усилий, не гарантия качества или расхода квоты.
Выбери доступную модель с указанной глубиной рассуждения; конкретные названия моделей
комплект не фиксирует. При ограниченной квоте запускай последовательно.

Каждый researcher пишет только свой `ideas/multi-brand-content/raw/TRACK/`:
evidence.jsonl, отчёт(ы) и run-status.json. Raw всегда PENDING.
Ориентир — до 45 минут discovery на track, с сохранением каждых нескольких записей;
это предел работы, а не требование ждать или набрать квоту.

COMPLETE означает завершённый поиск, а не пройденные gates. PARTIAL из-за квоты
или неполного охвата допустим; незаполненные вопросы остаются неизвестными.

## 5. Если снова начинается python -c / brain / cache

Отклони такую команду и передай:

> Stop this command. It is outside this Multi-brand run's exact terminal allowlist.
> Do not use python -c, inline code, Antigravity brain/generated steps or browser cache.
> Preserve authorized outputs and use only the checker command in the original
> Multi-brand launch prompt. If blocked, record the blocker and end partial.

Не удаляй разговор или результаты ради устранения петли. Останови writer.
Для продолжения используй исходный stage prompt и `90-resume.md`.
Auditor при восстановлении не получает права искать новые источники.

## 6. Checkpoint raw

После завершения всех пяти исследований:

```bash
python scripts/check_multibrand_stage1.py raw-all
git status --short
git add ideas/multi-brand-content/raw
git diff --cached --name-status
git commit -m "Checkpoint Multi-brand Stage 1 raw research"
```

Если проверка не прошла, остановись до commit/handoff и верни ошибку владельцу track.
Перед commit проверь весь staging: там не должно оказаться чужих ранее добавленных
изменений. PARTIAL research разрешён, ошибка структуры — нет.

Повторные URL/keys checker показывает как предупреждения. Их оценивает Auditor:
несколько speakers в одном thread могут быть независимы, а несколько URL одного
провайдера не создают независимый спрос.

## 7. Auditor

Новый conversation, High, `/browser` + `/evidence-audit`.
Prompt: `prompts/multi-brand-content/20-run-auditor.md`.

Результаты в `ideas/multi-brand-content/evidence/`:

- evidence.jsonl — все raw IDs, включая отклонённые.
- audit-summary.md — полнота проверки, сводные числа и нормализация дублей.
- high-impact-review.md — деньги, сильнейшие аргументы, substitutes и исключения.
- scope-map.json — принадлежность scope, SOLO/AGENCY/UNKNOWN и подтверждающие IDs.

```bash
python scripts/check_multibrand_stage1.py audit
```

Checker печатает `DATASET_SUMMARY` с пересчитанными количествами. Эти числа
должны совпадать с отчётами; использовать количество URL вместо покупателей нельзя.

Перед Judge просмотри high-impact-review.md и оригиналы решающих записей.
Особенно проверь: использование ≠ оплата; гипотетические сэкономленные часы ≠
фактический труд; весь SMM-ретейнер ≠ бюджет на production software;
описанная функция ≠ достаточно хорошее решение; неизвестный scope ≠ опровергнутый.

Если неверна исходная запись, исправляет её researcher. Новый источник также
собирает researcher, не Auditor. После любого изменения raw повторяются audit
и Judge; не запускай Judge параллельно с правками evidence.

## 8. Judge

Новый conversation, High, **без browser**, `/stage1-judge`.
Prompt: `prompts/multi-brand-content/30-run-judge.md`.

Результаты:

- `ideas/multi-brand-content/output/stage1-report.md`
- `ideas/multi-brand-content/output/scorecard.json`

```bash
python scripts/check_multibrand_stage1.py judge
```

Checker проверяет schema/provenance, IDs, категории расходов, сводные количества,
scope/form breakdown, числовые thresholds и согласованность verdict. Он не
проверяет правдивость источников, причинность или коммерческую привлекательность.

Недостаточный dataset без сильного опровержения → INSUFFICIENT EVIDENCE.
FAIL требует сильного подтверждённого противоречия. CONDITIONAL PASS нельзя
получить объединением нескольких неизвестных в один вопрос.
Все шесть gates должны относиться к одной объявленной задаче и аудитории.

## 9. Сохранить и принести результат

После успешной проверки:

```bash
git add ideas/multi-brand-content
git diff --cached --name-status
git commit -m "Complete Multi-brand Stage 1 audit and judgment"
git push -u origin validation/multi-brand-stage1-kit
```

Проверь staging до commit. Не используй force push; при несовместимом продвижении
ветки остановись и разбери историю. Команды git выполняет человек.

Принеси commit SHA, ветку и четыре файла:

1. `ideas/multi-brand-content/output/stage1-report.md`
2. `ideas/multi-brand-content/output/scorecard.json`
3. `ideas/multi-brand-content/evidence/evidence.jsonl`
4. `ideas/multi-brand-content/evidence/high-impact-review.md`

Остальные audit/raw файлы сохраняются рядом для независимого разбора.
Решение Judge — рекомендация; переход к Stage 2 обсуждаем после проверки.
Stage 1 не является разрешением строить MVP, закрывать ChillPup или останавливать
согласованную работу над его базовой версией и контентом сайта.
