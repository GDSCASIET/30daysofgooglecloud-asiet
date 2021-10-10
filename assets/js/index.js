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
                if (${member.qcomplete_no}<6){
                newRow.innerHTML = `
                    <div class="c-list__grid">
                        <div class="c-flag c-place u-bg--transparent">${i}</div>
                        <div class="c-media">
                        <a href="${member.qlabid}" rel="noopener" target="_blank">
                            <img class="c-avatar c-media__img" src="${member.dp}" />
                            </a>
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
                `;}
                if (${member.qcomplete_no}==12){
                newRow.innerHTML = `
                    <div class="c-list__grid">
                        <div class="c-flag c-place u-bg--transparent">${i}</div>
                        <div class="c-media">
                        <a href="${member.qlabid}" rel="noopener" target="_blank">
                            <img class="c-avatar c-media__img" src="${member.dp}" />
                            </a>
                            <div class="c-media__content">
                                <div class="c-media__title">${member.name}</div>
                                <a class="c-media__link ">Track 1 - ${member.track1}</a>
                                <br>
                                <br>
                                <a class="c-media__link ">Track 2 - ${member.track2}</a>
                                <br>
                                <p class="pmilestone">
                                <span class="s1milestone sall">Milestone</span>
                                <span class= "s2milestone sall">2</span>
                                <span class="s3milestone sall">Achieved</span>
                                </p>
                            </div>
                        </div>
                        <div class="u-text--right c-kudos">
                            <div class="u-mt--8">
                                <strong>${member.qcomplete_no}</strong>
                            </div>
                        </div>
                    </div>
                `;}
                if (${member.lentrack1}==6 || ${member.lentrack2}==6){
                newRow.innerHTML = `
                    <div class="c-list__grid">
                        <div class="c-flag c-place u-bg--transparent">${i}</div>
                        <div class="c-media">
                        <a href="${member.qlabid}" rel="noopener" target="_blank">
                            <img class="c-avatar c-media__img" src="${member.dp}" />
                            </a>
                            <div class="c-media__content">
                                <div class="c-media__title">${member.name}</div>
                                <a class="c-media__link ">Track 1 - ${member.track1}</a>
                                <br>
                                <br>
                                <a class="c-media__link ">Track 2 - ${member.track2}</a>
                                <br>
                                <p class="pmilestone">
                                <span class="s1milestone sall">Milestone</span>
                                <span class= "s2milestone sall">1</span>
                                <span class="s3milestone sall">Achieved</span>
                                </p>
                            </div>
                        </div>
                        <div class="u-text--right c-kudos">
                            <div class="u-mt--8">
                                <strong>${member.qcomplete_no}</strong>
                            </div>
                        </div>
                    </div>
                `;}
                i++;
                list.appendChild(newRow);
            });




        } else {
            console.log("Something went wrong.")
        }
    };
}
