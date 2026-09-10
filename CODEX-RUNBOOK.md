# Codex: настройка проекта и исправление аудита

Текущий этап после `4649a2f`: контрольные пакеты завершены, продолжаем проверку
оставшихся источников по разделу 6. Инженерный pipeline уже реализован.
Разделы 1–4 описывают исходную настройку поверх `241d043`; повторять её не нужно.

## Что настраиваем

| Место | Назначение |
| --- | --- |
| `AGENTS.md` в корне репозитория | Общие инструкции Codex для этого проекта: роли, границы правок, достоверность evidence. |
| `.agents/skills/audit-pipeline-repair/SKILL.md` | Процедура исправления генерации и проверки аудита. У Codex здесь **agents** во множественном числе. |
| `prompts/codex/` | Конкретные задания для запуска; их можно поручить прочитать по пути. |
| `docs/codex/audit-pipeline-repair.md` | Требования к реализации и контрольные случаи из 241d043. |
| `.agent/skills/` и `.agent/rules/` | Существующая настройка Antigravity; этот комплект её сохраняет. |

Codex читает проектный `AGENTS.md` и обнаруживает skills в `.agents/skills`.
Уровни инструкций описаны в [документации AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md),
а структура skills — в [документации skills](https://learn.chatgpt.com/docs/build-skills).

Пустой пользовательский `AGENTS.md` не является ошибкой. Правила этого репозитория
не нужно переносить в глобальный файл: иначе они будут влиять и на другие проекты.
Существующую пользовательскую папку `skills` не удаляем и не переименовываем.

Codex `.rules` управляют разрешениями на выполнение команд; это другой механизм,
чем Markdown-правила Antigravity. Для нашего задания новые `.rules` и изменение
режима разрешений не требуются. См. [документацию rules](https://learn.chatgpt.com/docs/agent-configuration/rules).

Для первого этапа не нужны браузер, MCP или установка плагинов: он работает с
локальными данными. Содержимое пользовательского `config.toml` по скриншоту
неизвестно, и менять его ради этого комплекта не нужно.

## 1. Применить комплект

В Git Bash из локального репозитория:

```bash
cd /c/Work/Projects/saas-validation-starter
git status --short
git log -1 --oneline
```

Команды ниже рассчитаны на чистую рабочую копию ветки с аудитом `241d043` в истории.
Если есть незакоммиченные изменения, сначала сохрани свою работу обычным способом;
не используй reset/clean для установки комплекта. Если уже существуют одноимённые
файлы настройки, сначала сравни их: не затирай свои инструкции.

Скачай `codex-audit-setup.patch`, затем создай отдельную ветку и примени patch.
Путь к Downloads замени, если файл сохранён в другом месте:

```bash
git switch -c validation/codex-audit-repair
git am /c/Users/acer/Downloads/codex-audit-setup.patch
git show --stat --oneline HEAD
```

`git am` добавляет локальный коммит с настройкой. Если применение остановилось
из-за конфликта, не начинай задачу Codex на частично установленном комплекте:
проверь конфликт; `git am --abort` отменяет именно незавершённое применение.

## 2. Новый conversation в Codex

Открой этот локальный проект и проверь выбранную ветку. Уже выбранные на скриншоте
GPT-5.6 Sol и High можно оставить для инженерного запуска; обещания безошибочного
аудита из выбора модели не следуют. Глобальные настройки разрешений оставь как есть.

После добавления `AGENTS.md` начни новый conversation. Не требуется переносить туда
весь старый диалог или подключать все исследовательские skills Antigravity.

Сначала отправь короткую проверку:

```text
Прочитай и выполни prompts/codex/00-check-setup.md.
```

Ожидаемый ответ: фактические путь, ветка, HEAD, состояние worktree и прочитанные
инструкции. Это проверка доступа к файлам, не доказательство автоматического
обнаружения skill или работы браузера. Если skill не виден в интерфейсе, перезапусти
приложение; явное чтение `SKILL.md` по пути достаточно для выполнения этого задания.
Не добавляй ради этого широкие глобальные правила `allow`.

## 3. Запустить инженерную задачу

Если проверка не выявила блокера, в том же новом conversation отправь:

```text
Прочитай AGENTS.md и .agents/skills/audit-pipeline-repair/SKILL.md.
Выполни prompts/codex/10-repair-audit-pipeline.md полностью:
реализуй инструменты и регрессионные тесты по docs/codex/audit-pipeline-repair.md.
```

Мы явно называем skill файлом, поэтому запуск не зависит от синтаксиса picker
в конкретной версии приложения. Команды Antigravity `/browser` и `/evidence-audit`
здесь не подразумеваются.

Этот запуск должен создать:

1. Структурированные source-review записи с привязкой к raw-версии и полученному
   фрагменту, а также отдельную очередь исправлений для владельцев raw.
2. Генератор журнала/отчёта и checker, сравнивающий данные, ссылки и totals.
3. Проверки известных ошибок и подготовку пакетов максимум по пять raw-ID.
4. Рабочий skill/prompt для следующего source review и проверенные CLI-команды.

В этом запуске `ideas/` остаётся без изменений. Старый аудит обязан показать
ошибки при новом строгом контроле, пока не появятся настоящие source-review
записи. Нельзя исправлять это заполнением выдуманных captures или механическим
переносом старых VERIFIED. Методология PASS/CONDITIONAL и границы ICP сохраняются.

## 4. Что принести после инженерного запуска

Проверь итоговый diff и результаты тестов. Убедись, что Codex перечислил ожидаемые
ошибки старого аудита и не объявил идею прошедшей Stage 1. Для проверки сохранности:

```bash
git diff --stat
git diff 241d043 -- ideas/
git status --short
```

Вторая команда должна быть пустой, если поверх 241d043 были только этот комплект
и инженерная задача. Если до запуска уже были другие правки `ideas/`, сравнивай с
зафиксированным состоянием на старте, сохраняя эти пользовательские изменения.

После просмотра сохрани реализацию своим обычным commit/push и пришли SHA вместе
с результатами тестов. Сначала проверим код и контракты, затем запустим отдельный
source-review conversation на контрольных пяти записях. Наличие работающего
доступа к оригинальным страницам проверяется перед тем запуском; нет доступа —
пакет остаётся частичным. Решение о Stage 2 принимается только после достоверного
аудита и Judge, а не после зелёных тестов инструментов.

## 5. Реализованный офлайн audit pipeline

Версия 1 контракта описана в `methodology/source-review-schema.json` и
`docs/codex/source-review-contract.md`. Рабочий CLI —
`scripts/audit_review_pipeline.py`. В текущей Windows-сессии `python` отсутствует
в `PATH`, поэтому проверенные команды используют bundled runtime Codex:

```powershell
$auditPython = 'C:\Users\acer\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $auditPython scripts/audit_review_pipeline.py legacy-diagnostic
& $auditPython -m unittest discover -s scripts -p 'test_check_multibrand_stage1.py'
& $auditPython -m unittest discover -s scripts -p 'test_audit_review_pipeline.py'
```

На неизменённом историческом наборе baseline diagnostic вычисляет из файлов 80
raw/audited/ledger строк, 59 различий exact URL, 51 различие independence key, а
также 63/65/66 exact URL в audited JSONL, ledger и старом narrative. После
авторизованной миграции эти числа закономерно изменятся: обычный regression test
использует фиксированную временную synthetic fixture, а не живые `ideas/`.
Это диагностика расхождений, не source verification.

После появления sidecar-файлов полный временный candidate создаётся и проверяется
так (пути можно заменить только на явные пути внутри репозитория):

```powershell
& $auditPython scripts/audit_review_pipeline.py render --reviews work/source-review/all --output work/audit-candidate
& $auditPython scripts/audit_review_pipeline.py check --reviews work/source-review/all --candidate work/audit-candidate
```

Для частичного checkpoint разрешён `--allow-incomplete` у обеих команд. Такой
candidate помечает отсутствующие/blocked строки PENDING, scope UNKNOWN и никогда
не является admission-ready. Обычные фазы `audit` и `judge` теперь всегда требуют
полное строгое покрытие в `ideas/multi-brand-content/evidence/source-reviews/` и
точное совпадение детерминированных отчётов. Поэтому неизменённый legacy audit
ожидаемо падает до Judge из-за отсутствия sidecar provenance.

Контрольный пакет подготавливается, но не исследуется в инженерном запуске:

```powershell
& $auditPython scripts/audit_review_pipeline.py prepare-batch --state-dir work/source-review/control-01 --ids mb-pain-001 mb-wtp-001 mb-wtp-005 mb-wtp-008 mb-wtp-009
```

Следующий conversation получает `prompts/codex/20-source-review-control-batch.md`.
После каждой фактической инспекции и при возобновлении используется одна команда:

```powershell
& $auditPython scripts/audit_review_pipeline.py checkpoint-batch --state-dir work/source-review/control-01
```

`batch-state.json` сохраняет processed, blocked и remaining IDs; повторный
`prepare-batch` с тем же порядком IDs не затирает прогресс. Исправления source
facts попадают в `raw-owner-repairs.jsonl`, а не применяются аудитором. Перенос
candidate в `ideas/`, raw repair и Judge требуют отдельных явно разрешённых задач.

После follow-up review `05de6b6` checkpoint сначала проверяет неизменность
завершённых reviews/captures и всех явных scope-support зависимостей. Только новые
или ранее blocked строки получают вычисленные derived hashes, причём запись на
диск происходит после полной валидации bundle. Judge сопоставляет каждый counted
и contradictory ID с `impact_assessment.eligible_gates`. Контрольные инженерные
воспроизведения запускаются так:

```powershell
& $auditPython scripts/reproduce_05de6b6.py --repo .
```

## 6. Продолжить аудит после контрольного пакета

`20-source-review-control-batch.md` и `21-resume-control-batch.md` сохраняются для
истории контрольного запуска и восстановления. Следующие пакеты используют
`prompts/codex/22-review-prepared-batch.md` с одним параметром `BATCH_DIR`.
Skill, checker, schema и market gates для этого перехода не меняются.

Состояние на базе `4649a2f`: проверены пять уникальных raw-ID из 80, остаются 75.
Новая проверка `mb-pain-001` в `control-01-scope-recheck` должна заменить старую
при отдельной консолидации; обе исторические версии сохраняются в своих пакетах.
Она не добавляет шестую evidence row. Ни один запуск ниже не выполняет эту
консолидацию и не переносит прежние VERIFIED автоматически.

### Ближайший запуск

Пакет `work/source-review/wtp-02/` уже подготовлен офлайн из canonical raw:

- `mb-wtp-002`
- `mb-wtp-003`
- `mb-wtp-004`
- `mb-wtp-006`
- `mb-wtp-007`

Его captures/reviews пусты, все пять ID находятся в remaining. Подготовка пакета
не является проверкой источников. Повторять `prepare-batch` для него не нужно.

В новом разговоре Codex отправь:

```text
Выполни prompts/codex/22-review-prepared-batch.md.
BATCH_DIR = work/source-review/wtp-02
Проверь только этот подготовленный пакет. После его checkpoint остановись.
```

При прерывании повтори тот же запуск: агент прочитает state и продолжит только
blocked/remaining, сохранив завершённые reviews. Если checkpoint не прошёл после
разрешённой структурной правки, сначала разбирается конкретный блокер; новый
разговор сам по себе не делает незапечатанную запись завершённой.

После этого пакета вне контрольной пятёрки остаётся ещё `mb-wtp-010`, а также
непроверенные IDs других треков. Следующий пакет определяется по каноническому
списку и уже завершённым review, а не по количеству файлов или captures.

### Последующие пакеты

Подготавливай только известные непроверенные ID, максимум пять на пакет, через
существующий `prepare-batch`. Это отдельная офлайн-подготовка, не команда внутри
ограниченного research-запуска. Например, для оставшегося WTP-ID:

```powershell
& 'C:\Users\acer\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts/audit_review_pipeline.py prepare-batch --state-dir work/source-review/wtp-03 --ids mb-wtp-010
```

Затем используй тот же промпт 22, меняя только параметр:

```text
Выполни prompts/codex/22-review-prepared-batch.md.
BATCH_DIR = work/source-review/wtp-03
Проверь только этот подготовленный пакет. После его checkpoint остановись.
```

Этот пример не утверждает, что `wtp-03` уже создан. Для pain/workflow/market/
skeptic нужен такой же заранее подготовленный пакет известных ID. Не запускай
два разговора с записью в одну директорию. Ревизии завершённых ID готовятся в
отдельных директориях с последующим явным выбором одной версии на raw-ID.

### Когда переходить к Judge

После покрытия всех 80 raw-ID нужна отдельная сборка актуальных reviews/captures,
разрешение ревизий и строгие `render/check`, затем перенос согласованного аудита
в canonical evidence в рамках отдельной задачи. Raw-owner actions нельзя
применять механически: изменение raw делает зависимые reviews устаревшими.
Если запись остаётся частично подтверждённой, её можно сохранить с этим статусом;
добиваться VERIFIED для каждой записи не требуется.

BLOCKED/PENDING и `--allow-incomplete` не дают разрешения на обычный Judge.
Полное покрытие аудита тоже не означает PASS: Judge использует только допустимые
свидетельства и существующие gates. Не меняй scope, пороги или код, чтобы получить
положительный результат.
