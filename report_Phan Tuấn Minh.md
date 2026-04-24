# Báo cáo cá nhân — Thành viên 3

**Họ và tên:** Phan Tuấn Minh
**MSV:** 2A202600422
**Vai trò:** DevOps & Integration Specialist (Orchestrator)  
**Độ dài:** ~450 từ

---

## 1. Phụ trách

Triển khai `orchestrator.py` — file "glue" kết nối toàn bộ pipeline. Đọc raw data → gọi Builder xử lý → gọi Watchman kiểm tra → lưu kết quả.

**Bằng chứng:** `starter_code/orchestrator.py`, `processed_knowledge_base.json`

---

## 2. Quyết định kỹ thuật

**Pipeline flow:** glob PDF files → process_pdf_data → run_semantic_checks → append to final_kb → tương tự cho Video files. Quyết định này tạo flow rõ ràng, dễ debug.

**Output format:** Lưu thành JSON List (`json.dump(final_kb, f, indent=4)`) — đúng format yêu cầu của test final_output_structure.

**Error handling:** Pipeline tiếp tục xử lý các file tiếp theo ngay cả khi một file lỗi (không crash) → đảm bảo robustness.

---

## 3. Sự cố / anomaly

**File not found:** Cần đảm bảo đường dẫn RAW_DATA_DIR và OUTPUT_FILE chính xác. Sử dụng `os.path.join(BASE_DIR, "..", "raw_data")` để navigate từ starter_code ra root.

**Quality check integration:** Ban đầu chưa gọi run_semantic_checks sau khi process → sau đó bổ sung logic: `if run_semantic_checks(processed_doc): final_kb.append(processed_doc)`

---

## 4. Before/after

**Before:** Không có file output  
**After:** Tạo `processed_knowledge_base.json` với 2 bản ghi hợp lệ, log: `Pipeline finished! Saved 2 records.`

---

## 5. Cải tiến thêm

Có thể thêm logging chi tiết hơn (file nào pass, file nào fail, lý do gì) để tiện theo dõi và debug khi mở rộng pipeline.