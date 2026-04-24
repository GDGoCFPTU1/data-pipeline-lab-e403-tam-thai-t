# Báo cáo cá nhân — Thành viên 1

**Họ và tên:** Vũ Tiến Thành
**MSV:** 2A202600443 
**Vai trò:** Lead Data Architect + ETL/ELT Builder  

---

## 1. Phụ trách

Triển khai hai file chính: `schema.py` (Architect) và `process_unstructured.py` (Builder). Đây là nền tảng của toàn bộ pipeline — schema định nghĩa "hợp đồng dữ liệu" và builder chuyển đổi dữ liệu thô về đúng format.

**Bằng chứng:** `starter_code/schema.py`, `starter_code/process_unstructured.py`

---

## 2. Quyết định kỹ thuật

**UnifiedDocument Schema (6 trường):** `document_id`, `source_type`, `author`, `category`, `content`, `timestamp`. Quyết định này đảm bảo cả PDF và Video data sau khi xử lý đều có cùng cấu trúc, thuận tiện cho AI agent query.

**Regex cleaning:** Sử dụng `re.sub(r'HEADER_PAGE_\d+\s*', '', raw_text)` và `re.sub(r'FOOTER_PAGE_\d+\s*', '', cleaned_content)` để loại bỏ noise từ OCR output. Quyết định này giúp content sạch sẽ, không có metadata không cần thiết.

**Schema mapping:** PDF (docId→document_id, authorName→author, docCategory→category, extractedText→content, createdAt→timestamp) và Video (video_id→document_id, creator_name→author, transcript→content).

---

## 3. Sự cố / anomaly

**doc2_corrupt.json:** Chứa "Null pointer exception" — ban đầu chưa xử lý toxic content. Sau khi phối hợp với Watchman bổ sung quality check, file này bị reject đúng cách.

**vid2_missing_tags.json:** Thiếu transcript → content rỗng → bị quality gate loại bỏ.

---

## 4. Before/after

**Before:** Raw data với camelCase, snake_case lộn xen, có HEADER_PAGE_X, FOOTER_PAGE_X  
**After:** Unified schema 6 trường, content đã làm sạch, 2/4 records pass quality gates

---

## 5. Cải tiến thêm

Có thể thêm timestamp format validation (ISO 8601) để đảm bảo downstream AI parse được thời gian chính xác.