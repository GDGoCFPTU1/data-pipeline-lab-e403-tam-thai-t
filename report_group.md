# Báo cáo nhóm — Data Pipeline Engineering

**Thành viên nhóm:** 3 người  
**Ngày nộp:** 24/04/2026  
**Điểm đạt được:** 100/100

---

## Tổng quan dự án

Xây dựng đường ống dữ liệu (Data Pipeline) tự động để ingest, làm sạch, kiểm tra chất lượng và hợp nhất dữ liệu từ hai nguồn: PDF (OCR text) và Video (metadata & transcript) thành Knowledge Base thống nhất cho AI Agent.

---

## Phân công công việc

| Thành viên | Vai trò | File phụ trách |
|------------|---------|----------------|
| Vũ Tiến Thành | Lead Data Architect + ETL Builder | schema.py, process_unstructured.py |
| Nguyễn Mậu Lân | Observability & QA Engineer | quality_check.py |
| Phan Tuấn Minh | DevOps & Integration Specialist | orchestrator.py |

---

## Kiến trúc hệ thống

```
raw_data/
├── group_a_pdfs/ (doc1_messy.json, doc2_corrupt.json)
└── group_b_videos/ (vid1_metadata.json, vid2_missing_tags.json)
        ↓
[Orchestrator] → [Builder: process_unstructured.py] → [Watchman: quality_check.py] → [Knowledge Base]
```

---

## Kết quả xử lý

| File | Nguồn | Kết quả | Lý do |
|------|-------|---------|-------|
| doc1_messy.json | PDF |  Pass | Đã làm sạch HEADER/FOOTER |
| doc2_corrupt.json | PDF |  Reject | Toxic: "Null pointer exception" |
| vid1_metadata.json | Video |  Pass | Đầy đủ fields |
| vid2_missing_tags.json | Video |  Reject | Thiếu transcript (content < 10 ký tự) |

**Output:** `processed_knowledge_base.json` — 2 bản ghi hợp lệ

---

## Các quyết định kỹ thuật quan trọng

1. **UnifiedDocument Schema (6 trường):** document_id, source_type, author, category, content, timestamp — đảm bảo harmonization giữa PDF và Video

2. **Regex cleaning:** Loại bỏ HEADER_PAGE_X, FOOTER_PAGE_X khỏi PDF text

3. **Quality Gates:** Kiểm tra content length < 10 ký tự và toxic keywords

4. **Idempotency:** Pipeline chạy deterministic, không phụ thuộc thứ tự

---

## Thách thức và giải pháp

- **Thách thức:** doc2_corrupt.json chứa lỗi OCR → **Giải pháp:** Bổ sung toxic keywords detection
- **Thách thức:** vid2_missing_tags.json thiếu transcript → **Giải pháp:** Thêm content length validation

---

## Kết luận

Nhóm hoàn thành 100% yêu cầu bài lab với pipeline chạy trơn tru, đúng schema, quality gates hoạt động, và output đúng định dạng.