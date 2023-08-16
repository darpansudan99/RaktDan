document.addEventListener('DOMContentLoaded', ()=>{

    loadPage('Select Your City');

    document.querySelector('#submit1').addEventListener('click', ()=>{
        city = document.querySelector('#drop1').value;
        loadPage(city);
    });

    if(document.querySelector('#submit2') !== null){
        document.querySelector('#submit2').addEventListener('click', ()=>{
            btype = document.querySelector('#drop2').value;
            fetch(`/getunits/${btype}`)
            .then(response => response.json())
            .then(response => {
                const bh = document.createElement('b');
                bh.style = "padding-left: 10px; padding-bottom: 10px; font-size: 1.5em;";
                bh.innerHTML = `Units of Blood Type ${btype}`;

                const table = document.createElement('table');
                table.classList.add('table');

                const r1 = document.createElement('tr');

                const c1 = document.createElement('th');
                c1.innerHTML = 'Blood Bank';

                const c2 = document.createElement('th');
                c2.innerHTML = 'City';

                const c3 = document.createElement('th');
                c3.style = "text-align: center;";
                c3.innerHTML = 'Number of Units';

                r1.append(c1, c2, c3);

                table.append(r1);

                response.rows.forEach(row => {
                    const r = document.createElement('tr');

                    const cl1 = document.createElement('td');
                    const a1 = document.createElement('a');
                    a1.innerHTML = row.blood_bank;
                    a1.href = `/bloodBank/${row.blood_bank}`;
                    cl1.append(a1);

                    const cl2 = document.createElement('td');
                    cl2.innerHTML = row.city;

                    const cl3 = document.createElement('td');
                    cl3.style = "text-align: center;";
                    cl3.innerHTML = row.no_of_units;

                    r.append(cl1, cl2, cl3);

                    table.append(r);
                });

                document.querySelector('#unitr').append(bh, table);

            });
        });
    }
})

function loadPage(city){

    fetch(`/filter/${city}`)
        .then(response => response.json())
        .then(response => {
            const br1 = document.createElement('br');
            const br2 = document.createElement('br');

            const list = document.querySelector('#list');
            list.innerHTML = "";

            const cmp = document.createElement('h1');
            cmp.innerHTML = 'Donation Camps';

            const campHeading = document.createElement('div');
            campHeading.classList = 'card';
            campHeading.style = "display:flex; flex-flow: row wrap; justify-content: space-between; padding-right: 4%;";

            const b1 = document.createElement('b');
            b1.innerHTML = 'Camp';
            const b2 = document.createElement('b');
            b2.innerHTML = 'Schedule';
            const b3 = document.createElement('b');
            b3.innerHTML = 'Address';
            const b4 = document.createElement('b');
            b4.innerHTML = 'Contact No.';

            campHeading.append(b1, b2, b3, b4);

            list.append(cmp, campHeading);
            response.camps.forEach(camp => showCamp(camp));

            const bnk = document.createElement('h1');
            bnk.innerHTML = 'Blood Banks';
            const card1 = document.createElement('div');
            card1.classList = 'card';
            card1.id = 'bank';
            list.append(br1, bnk, card1);
            response.banks.forEach(bank => showBank(bank));

            const hsp = document.createElement('h1');
            hsp.innerHTML = 'Hospitals';
            const card2 = document.createElement('div');
            card2.classList = 'card';
            card2.id = 'hosp';
            list.append(br2, hsp, card2);
            response.hospitals.forEach(hospiital => showHosp(hospiital));
        });
}

function showCamp(camp){
    const div0 = document.createElement('div');
    div0.classList = 'card';
    div0.style = "display:flex; flex-flow: row wrap; justify-content: space-between;  padding-right: 4%;";

    const div1 = document.createElement('div');
    div1.innerHTML = camp.name;

    const div2 = document.createElement('div');
    div2.innerHTML = `${camp.start_date} to ${camp.end_date}`;

    const div3 = document.createElement('div');
    div3.innerHTML = `${camp.street}, ${camp.city}, ${camp.state}`;

    const div4 = document.createElement('div');
    div4.innerHTML = camp.phone_no;

    div0.append(div1, div2, div3, div4);
    document.querySelector('#list').append(div0);
}

function showBank(bank){
    const div0 = document.createElement('div');
    div0.style = "display:flex; flex-flow: row wrap; justify-content: space-between;";

    const div1 = document.createElement('a');
    div1.innerHTML = bank.name;
    div1.href = `/bloodBank/${bank.name}`;

    const div2 = document.createElement('div');
    div2.innerHTML = bank.city;

    const hr = document.createElement('hr');

    div0.append(div1, div2);
    document.querySelector('#bank').append(div0, hr);
}

function showHosp(hosp){
    const div0 = document.createElement('div');
    div0.style = "display:flex; flex-flow: row wrap; justify-content: space-between;";

    const div1 = document.createElement('a');
    div1.innerHTML = hosp.name;
    div1.href = `/profile/${hosp.name}`;

    const div2 = document.createElement('div');
    div2.innerHTML = hosp.city;

    const hr = document.createElement('hr');

    div0.append(div1, div2);
    document.querySelector('#hosp').append(div0, hr);
}