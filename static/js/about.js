$(document).ready(function() {
    const $stageImages = $('.stage-image');
    const $stageDescription = $('.stage-description');
    let currentStageIndex = 0;

    function updateStage() {
        const currentStage = $stageImages.eq(currentStageIndex);
        const description = currentStage.data('description');
        const index = currentStage.data('index');
        $('.stage-image').removeClass('highlight');
        currentStage.addClass('highlight');
        $('#stageImage').attr('src', currentStage.attr('src'));
        $stageDescription.text(description);
    }

    updateStage(); // Initial update

    $('#nextStageBtn').click(function() {
        currentStageIndex = (currentStageIndex + 1) % $stageImages.length;
        updateStage();
    });

    $('#prevStageBtn').click(function() {
        currentStageIndex = (currentStageIndex - 1 + $stageImages.length) % $stageImages.length;
        updateStage();
    });
});
