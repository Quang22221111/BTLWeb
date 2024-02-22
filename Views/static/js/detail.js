function toggleExpand() {
    var block = document.getElementById("expandableBlock");
    block.classList.toggle("expanded");
    var button = block.querySelector("button");
  
    // Thay đổi nội dung văn bản của nút
    if (block.classList.contains("expanded")) {
      button.textContent = "Xem Thêm";
    } else {
      button.textContent = "Thu gọn";
    }
  }
