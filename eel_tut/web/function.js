// This script will be called when the confirm button is clicked
 document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('confirmButton').addEventListener('click', function() {
        var chapter = document.getElementById('chapterSelect').value;
        eel.get_random_question_from_chapter(chapter)(displayQuestion);
    });
});
// This function receives the random question and redirects to QuestionPage.html
function displayQuestion(questionData) {
    // Store the question data and chapter number in session storage
    sessionStorage.setItem('currentQuestion', JSON.stringify(questionData));
    var chapter = document.getElementById('chapterSelect').value;
    sessionStorage.setItem('currentChapter', JSON.stringify(chapter));

    // Redirect to QuestionPage.html
    window.location.href = 'QuestionPage.html';
}
