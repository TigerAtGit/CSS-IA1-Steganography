const actualBtn = document.getElementById('actualbtn');

const fileChosen = document.getElementById('filechosen');

actualBtn.addEventListener('change', function() {
    fileChosen.textContent = this.files[0].name
})

const actualBtn3 = document.getElementById('actualbtn3');

const fileChosen3 = document.getElementById('filechosen3');

actualBtn3.addEventListener('change', function() {
    fileChosen3.textContent = this.files[0].name
})

const actualBtn2 = document.getElementById('actualbtn2');

const fileChosen2 = document.getElementById('filechosen2');

actualBtn2.addEventListener('change', function() {
    fileChosen2.textContent = this.files[0].name
})

document.querySelector('.img__btn').addEventListener('click', function() {
    document.querySelector('.cont').classList.toggle('s--signup');
});

$('#OpenImgUpload').click(function() { $('#imgupload').trigger('click'); });


var inputs = document.querySelectorAll('.inputfile');
Array.prototype.forEach.call(inputs, function(input) {
    var label = input.nextElementSibling,
        labelVal = label.innerHTML;

    input.addEventListener('change', function(e) {
        var fileName = '';
        if (this.files && this.files.length > 1)
            fileName = (this.getAttribute('data-multiple-caption') || '').replace('{count}', this.files.length);
        // else{
        // 	fileName = e.target.value.split( '\' ).pop();}

        if (fileName)
            label.querySelector('span').innerHTML = fileName;
        else
            label.innerHTML = labelVal;
    });
});