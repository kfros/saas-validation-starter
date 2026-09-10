# Multi-brand: готовые сообщения для проверки оставшихся источников

Подготовлено офлайн поверх `37af6cc2f8227ad140ad50784be202665790bb58`.
Снимок canonical raw: `95fbe75c0ce6051a9df9ebc919a11cedcc8fe26928da8a9b113ebd38a2627806`.

Все пакеты ниже уже подготовлены. Запускать `prepare-batch` и выбирать ID вручную не нужно.
Это статический порядок запуска; фактический прогресс хранится в `batch-state.json` каждого пакета.

На момент подготовки: 80 raw-ID, 5 уникальных ID проверены в контрольных пакетах,
75 распределены без пропусков и повторов по 15 пакетам по пять. Пакет `wtp-02` сохранён
из предыдущего комплекта; остальные 14 созданы здесь. Captures/reviews новых пакетов пусты.
Источники во время подготовки не открывались, рыночные решения не принимались.

## Как запускать

1. Используй один локальный checkout и текущую ветку с применёнными комплектами.
   Каждый новый пакет запускай в новом разговоре Codex, последовательно.
2. Копируй очередной блок целиком. Он уже содержит нужный `BATCH_DIR`; ничего менять не нужно.
   Если `wtp-02` уже завершён, начинай со второго сообщения.
3. После успешного checkpoint со всеми пятью processed и пустыми blocked/remaining
   сохрани изменения обычным commit и переходи к следующему сообщению.
4. При прерывании используй тот же блок для того же пакета. Рабочий разговор можно
   продолжить; после зависания открой новый. Завершённые записи восстанавливаются из файлов.
   При повторном структурном сбое после разрешённой правки сохрани диагностику и остановись:
   повторение сообщения не должно превращаться в бесконечный ремонт.
5. После последнего пакета остановись: консолидация, выбор ревизий, итоговый audit
   и Judge выполняются отдельными задачами.

Каждый блок запускает промпт `22-review-prepared-batch.md`; новый skill не нужен.
Не записывай из двух разговоров в один пакет. Если raw изменится, устаревший snapshot
должен стать видимым блокером; не переподготавливай пакет для обхода проверки.

## Порядок и ID

| Запуск | BATCH_DIR | Raw-ID |
| --- | --- | --- |
| 1 | `work/source-review/wtp-02` | `mb-wtp-002`, `mb-wtp-003`, `mb-wtp-004`, `mb-wtp-006`, `mb-wtp-007` |
| 2 | `work/source-review/batch-03` | `mb-wtp-010`, `mb-pain-002`, `mb-pain-003`, `mb-pain-004`, `mb-pain-005` |
| 3 | `work/source-review/batch-04` | `mb-pain-006`, `mb-pain-007`, `mb-pain-008`, `mb-pain-009`, `mb-pain-010` |
| 4 | `work/source-review/batch-05` | `mb-pain-011`, `mb-pain-012`, `mb-pain-013`, `mb-pain-014`, `mb-pain-015` |
| 5 | `work/source-review/batch-06` | `mb-pain-016`, `mb-pain-017`, `mb-pain-018`, `mb-pain-019`, `mb-pain-020` |
| 6 | `work/source-review/batch-07` | `mb-pain-021`, `mb-workflow-001`, `mb-workflow-002`, `mb-workflow-003`, `mb-workflow-004` |
| 7 | `work/source-review/batch-08` | `mb-workflow-005`, `mb-workflow-006`, `mb-workflow-007`, `mb-workflow-008`, `mb-workflow-009` |
| 8 | `work/source-review/batch-09` | `mb-workflow-010`, `mb-workflow-011`, `mb-workflow-012`, `mb-workflow-013`, `mb-workflow-014` |
| 9 | `work/source-review/batch-10` | `mb-skeptic-001`, `mb-skeptic-002`, `mb-skeptic-003`, `mb-skeptic-004`, `mb-skeptic-005` |
| 10 | `work/source-review/batch-11` | `mb-skeptic-006`, `mb-skeptic-007`, `mb-skeptic-008`, `mb-skeptic-009`, `mb-skeptic-010` |
| 11 | `work/source-review/batch-12` | `mb-skeptic-011`, `mb-skeptic-012`, `mb-skeptic-013`, `mb-skeptic-014`, `mb-market-001` |
| 12 | `work/source-review/batch-13` | `mb-market-002`, `mb-market-003`, `mb-market-004`, `mb-market-005`, `mb-market-006` |
| 13 | `work/source-review/batch-14` | `mb-market-007`, `mb-market-008`, `mb-market-009`, `mb-market-010`, `mb-market-011` |
| 14 | `work/source-review/batch-15` | `mb-market-012`, `mb-market-013`, `mb-market-014`, `mb-market-015`, `mb-market-016` |
| 15 | `work/source-review/batch-16` | `mb-market-017`, `mb-market-018`, `mb-market-019`, `mb-market-020`, `mb-market-021` |

Смешанные пакеты на границах треков заполняют все пять мест. Каждая запись сохраняет
свой raw track, источник и автора; совместное размещение не делает записи независимыми
и не объединяет их утверждения. В частности, `mb-wtp-010` находится во втором пакете
вместе с четырьмя pain-ID.

## Сообщения

### 01. wtp-02

```text
Выполни prompts/codex/22-review-prepared-batch.md.
BATCH_DIR = work/source-review/wtp-02
Проверь только этот подготовленный пакет.
После его checkpoint остановись.
```

### 02. batch-03

```text
Выполни prompts/codex/22-review-prepared-batch.md.
BATCH_DIR = work/source-review/batch-03
Проверь только этот подготовленный пакет.
После его checkpoint остановись.
```

### 03. batch-04

```text
Выполни prompts/codex/22-review-prepared-batch.md.
BATCH_DIR = work/source-review/batch-04
Проверь только этот подготовленный пакет.
После его checkpoint остановись.
```

### 04. batch-05

```text
Выполни prompts/codex/22-review-prepared-batch.md.
BATCH_DIR = work/source-review/batch-05
Проверь только этот подготовленный пакет.
После его checkpoint остановись.
```

### 05. batch-06

```text
Выполни prompts/codex/22-review-prepared-batch.md.
BATCH_DIR = work/source-review/batch-06
Проверь только этот подготовленный пакет.
После его checkpoint остановись.
```

### 06. batch-07

```text
Выполни prompts/codex/22-review-prepared-batch.md.
BATCH_DIR = work/source-review/batch-07
Проверь только этот подготовленный пакет.
После его checkpoint остановись.
```

### 07. batch-08

```text
Выполни prompts/codex/22-review-prepared-batch.md.
BATCH_DIR = work/source-review/batch-08
Проверь только этот подготовленный пакет.
После его checkpoint остановись.
```

### 08. batch-09

```text
Выполни prompts/codex/22-review-prepared-batch.md.
BATCH_DIR = work/source-review/batch-09
Проверь только этот подготовленный пакет.
После его checkpoint остановись.
```

### 09. batch-10

```text
Выполни prompts/codex/22-review-prepared-batch.md.
BATCH_DIR = work/source-review/batch-10
Проверь только этот подготовленный пакет.
После его checkpoint остановись.
```

### 10. batch-11

```text
Выполни prompts/codex/22-review-prepared-batch.md.
BATCH_DIR = work/source-review/batch-11
Проверь только этот подготовленный пакет.
После его checkpoint остановись.
```

### 11. batch-12

```text
Выполни prompts/codex/22-review-prepared-batch.md.
BATCH_DIR = work/source-review/batch-12
Проверь только этот подготовленный пакет.
После его checkpoint остановись.
```

### 12. batch-13

```text
Выполни prompts/codex/22-review-prepared-batch.md.
BATCH_DIR = work/source-review/batch-13
Проверь только этот подготовленный пакет.
После его checkpoint остановись.
```

### 13. batch-14

```text
Выполни prompts/codex/22-review-prepared-batch.md.
BATCH_DIR = work/source-review/batch-14
Проверь только этот подготовленный пакет.
После его checkpoint остановись.
```

### 14. batch-15

```text
Выполни prompts/codex/22-review-prepared-batch.md.
BATCH_DIR = work/source-review/batch-15
Проверь только этот подготовленный пакет.
После его checkpoint остановись.
```

### 15. batch-16

```text
Выполни prompts/codex/22-review-prepared-batch.md.
BATCH_DIR = work/source-review/batch-16
Проверь только этот подготовленный пакет.
После его checkpoint остановись.
```

## Что сохранить для итоговой сборки

Все 15 пакетов, исходный `control-01` и `control-01-scope-recheck` сохраняются.
При отдельной консолидации новая pain-ревизия должна заменить старую для
`mb-pain-001`; две версии не считаются двумя evidence rows.
Raw-owner actions пока остаются очередью, а частично подтверждённые записи
сохраняют честный статус. Количество проверенных записей не означает прохождение gates.
