console.clear();

function getData() {
    var xh = new XMLHttpRequest();
    xh.open(
        "GET",
        "my.json",
        true
    );
    xh.setRequestHeader("Content-Type", "application/json");
    xh.send();
    xh.onload = function () {
        if (this.status == 200) {
            // // console.log(this.responseText)
            var data = JSON.parse(this.responseText);
            console.log(data);

            var i = 1;
            data.forEach(member => {
                let newRow = document.createElement('li');
                newRow.classList = 'c-list__item';
                newRow.innerHTML = `
                    <div class="c-list__grid">
                        <div class="c-flag c-place u-bg--transparent">${i}</div>
                        <div class="c-media">
                            <img class="c-avatar c-media__img" src="${member.dp}" />
                            <div class="c-media__content">
                                <div class="c-media__title">${member.name}</div>
                                <a class="c-media__link ">Track 1 - ${member.track1}</a>
                                <br>
                                <br>
                                <a class="c-media__link ">Track 2 - ${member.track2}</a>
                            </div>
                        </div>
                        <div class="u-text--right c-kudos">
                            <div class="u-mt--8">
                                <strong>${member.qcomplete_no}</strong>
                            </div>
                        </div>
                    </div>
                `;
                if (i === 1) {
                    newRow.querySelector('.c-place').classList.add('u-text--dark');
                    newRow.querySelector('.c-place').classList.add('u-bg--yellow');
                    newRow.querySelector('.c-kudos').classList.add('u-text--yellow');
                } else if (i === 2) {
                    newRow.querySelector('.c-place').classList.add('u-text--dark');
                    newRow.querySelector('.c-place').classList.add('u-bg--teal');
                    newRow.querySelector('.c-kudos').classList.add('u-text--teal');
                } else if (i === 3) {
                    newRow.querySelector('.c-place').classList.add('u-text--dark');
                    newRow.querySelector('.c-place').classList.add('u-bg--orange');
                    newRow.querySelector('.c-kudos').classList.add('u-text--orange');
                }
                i++;
                list.appendChild(newRow);
            });




        } else {
            console.log("Something went wrong.")
        }
    };
}
