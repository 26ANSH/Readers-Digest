function toggleAvail() {
    quantity = parseInt(document.getElementById('bookQuantity').innerHTML)
    issue = parseInt(document.getElementById('bookIssue').innerHTML)
    available = document.getElementById('bookAvailability')

    if (issue >= quantity) {
        if (!(available.classList.contains('text-red-500'))) {
            available.classList.remove('text-green-500')
            available.classList.add('text-red-500')
        }

        available.innerHTML = `Not Available <i class="text-lg fas fa-thumbs-down"></i>`
    }
    else {
        if (!(available.classList.contains('text-green-500'))) {
            available.classList.remove('text-red-500')
            available.classList.add('text-green-500')
        }

        available.innerHTML = `Available <i class="text-lg fas fa-thumbs-up"></i>`
    }
}

function selectTypeChange(id) {
    fetch('/api/member/' + id, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (response) {
        if (response.status == 200) {
            return response.json();
        }
        else {
            document.getElementById('details').textContent = "Wrong Member ID"
            return false;
        }
    }).then(function (data) {
        if (data != false) {
            document.getElementById('details').textContent = data.user.name + " | Credits: " + data.user.credit
        }
    });
}

function returnBook(id) {
    fetch('/members/transactions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id: id,
            status: false
        })
    }).then(function (response) {
        return response.json();
    }).then(function (data) {
        if (data.code == 200) {
            document.getElementById(id).remove()
            document.getElementById('bookIssue').innerHTML = parseInt(document.getElementById('bookIssue').innerHTML) - 1
            toggleAvail()
        }
        else {
            document.getElementById('result').innerHTML = data.msg
        }
    });
}

// function issueBook() {
//     member = document.getElementById("member").value
//     fetch('/members/transactions', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({
//             member_id: member,
//             book_id: {{ book.id }},
//         status: true
//             })
//           }).then(function (response) {
//             return response.json();
//         }).then(function (data) {
//             if (data.code == 200) {
//                 document.getElementById('bookIssue').innerHTML = parseInt(document.getElementById('bookIssue').innerHTML) + 1
//                 toggleAvail()
//                 const t = data.msg
//                 var date = new Date(t.issued)
//                 date = date.toISOString().substring(0, 10);
//                 document.getElementById('usersTableContent').innerHTML += ` <tr id="${t.id}" class="border-blue-900 border-2 border-t-0 mb-2 sm:mb-0 hover:bg-blue-50 mb-2">
//                     <td class="border-blue-900 border p-2 text-center">${t.id}</td>
//                     <td class="border-blue-900 border p-2 text-center">${t.member} </td>
//                     <td class="border-blue-900 border p-2 text-center">${date}</td>
//                     <td class="border-blue-900 border p-2 text-center">${t.status} </td>
//                     <td class="border-blue-900 border p-2 text-center">${t.rent}</td>
//             <td class="border-blue-900 border p-2 text-center">
//                 <button onclick="returnBook(${t.id})" class="text-white rounded-md font-bold px-2 hover:bg-red-600 py-1 bg-red-700">Return</button>
//             </td>
//                   </tr>`
//             }
//             else {
//                 document.getElementById('result').innerHTML = data.msg
//             }
//         });
// }