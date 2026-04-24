# Báo cáo cá nhân — Thành viên 2

**Họ và tên:** Nguyễn Mậu Lân
**MSV:** 2A202600400 
**Vai trò:** Observability & QA Engineer (Quality Gates)  
**Độ dài:** ~450 từ

---

## 1. Phụ trách

Triển khai `quality_check.py` với hàm `run_semantic_checks()`. Đây là "cổng canh giữ" (Quality Gates) đảm bảo chỉ có dữ liệu chất lượng được đưa vào Knowledge Base cuối cùng.

**Bằng chứng:** `starter_code/quality_check.py`

---

## 2. Quyết định kỹ thuật

**Content length check:** Nếu content trống hoặc < 10 ký tự → return False. Quyết định này đảm bảo không có bản ghi rỗng hoặc quá ngắn (như vid2_missing_tags.json không có transcript).

**Toxic keywords detection:** Duyệt qua danh sách `["Null pointer exception", "OCR Error", "Traceback"]`, nếu từ nào xuất hiện trong content → return False. Quyết định này loại bỏ các bản ghi lỗi từ OCR engine (như doc2_corrupt.json).

**Fail-fast strategy:** Khi phát hiện lỗi, return False ngay lập tức thay vì tiếp tục kiểm tra các điều kiện khác → tối ưu hiệu năng.

---

## 3. Sự cố / anomaly

**doc2_corrupt.json:** File chứa "Null pointer exception during OCR process." — bị quality check phát hiện và reject. Đây là case toxic content điển hình.

**vid2_missing_tags.json:** Không có transcript → content = "" → bị length check reject.

---

## 4. Before/after

**Before:** Pipeline đưa tất cả 4 file vào output  
**After:** Chỉ 2/4 file pass quality gates (doc1_messy, vid1_metadata) → `Pipeline finished! Saved 2 records.`

---

## 5. Cải tiến thêm

Có thể mở rộng thêm các quality rules: kiểm tra timestamp format, validate category không rỗng, hoặc log chi tiết hơn cho từng loại lỗi để tiện debug.