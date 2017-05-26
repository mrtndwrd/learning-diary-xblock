/* Javascript for LearningDiary. */
function LearningDiary(runtime, element) {

    function updateCount(result) {
        $('.count', element).text(result.count);
    }

    function updateDiary(result) {
        $('#diary_txtinput', element).text(result.diary);
    }

    var handlerUrl = runtime.handlerUrl(element, 'increment_count');

    var handlerUrlDiary = runtime.handlerUrl(element, 'update_diary');

    $('p', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"hello": "world"}),
            success: updateCount
        });
    });

    $('#mybtn', element).click(function(eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrlDiary,
            data: JSON.stringify({"hello": "world"}),
            success: updateDiary
        });
    });


    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
