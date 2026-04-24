from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn (document_id, source_type, author, category, content, timestamp). 
    TODO: Khai báo các trường với kiểu dữ liệu str ở dưới.
    """
    document_id: str = Field(..., description="Unique identifier for the document")
    source_type: str = Field(..., description="Source type: PDF or Video")
    author: str = Field(..., description="Author or creator name")
    category: str = Field(..., description="Document category")
    content: str = Field(..., description="Processed content text")
    timestamp: str = Field(..., description="Creation timestamp")
