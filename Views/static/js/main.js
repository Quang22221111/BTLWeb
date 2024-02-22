var userComments = {};

function showComments(frameNumber) {
    // Ẩn tất cả các khung chứa bình luận
    var commentFrames = document.querySelectorAll(".comment-frame");
    commentFrames.forEach(function(frame) {
        frame.style.display = "none";
    });

    // Hiển thị khung chứa bình luận tương ứng với số được click
    var selectedFrame = document.getElementById("comment-frame-" + frameNumber);
    if (selectedFrame) {
        selectedFrame.style.display = "block";
        displayComments(frameNumber);
    }
}

function displayComments(frameNumber) {
    var commentsContainer = document.getElementById("comments-" + frameNumber);
    commentsContainer.innerHTML = "";

    if (userComments[frameNumber]) {
        userComments[frameNumber].forEach(function(comment) {
            var commentDiv = document.createElement("div");
            commentDiv.className = "comment";
            commentDiv.textContent = comment;
            commentsContainer.appendChild(commentDiv);
        });
    }
}

function addComment(frameNumber) {
    var newCommentInput = document.getElementById("new-comment-" + frameNumber);
    var newComment = newCommentInput.value;

    if (newComment.trim() !== "") {
        if (!userComments[frameNumber]) {
            userComments[frameNumber] = [];
        }

        userComments[frameNumber].push(newComment);
        displayComments(frameNumber);

        // Reset input field
        newCommentInput.value = "";
    }
}

function hideComments() {
    // Ẩn tất cả các khung chứa bình luận khi click bên ngoài chúng
    var commentFrames = document.querySelectorAll(".comment-frame");
    commentFrames.forEach(function(frame) {
        frame.style.display = "none";
    });
}

function updatePreview(frameNumber) {
    var newCommentInput = document.getElementById("new-comment-" + frameNumber);
    var previewContainer = document.getElementById("comments-" + frameNumber);
    previewContainer.textContent = newCommentInput.value;
}