// // // document.addEventListener('DOMContentLoaded', () => {
// // //     fetch('http://demo01.com:8003/api/method/estate_app.estate_plan.api.student_api.get_students')
// // //         .then(response => response.json())
// // //         .then(students => {
// // //             const studentList = document.getElementById('student-list');
            
// // //             students.message.forEach(student => {
// // //                 const studentCard = document.createElement('div');
// // //                 studentCard.classList.add('student-card');
// // //                 studentCard.innerHTML = `
// // //                     <p><strong>Register Number:</strong> ${student.register_number}</p>
// // //                     <p><strong>Name:</strong> ${student.name1 || 'Not Available'}</p>
// // //                     <p><strong>Date of Birth:</strong> ${student.date_of_birth || 'Not Available'}</p>
// // //                     <p><strong>Gender:</strong> ${student.gender || 'Not Available'}</p>
// // //                     <p><strong>Email:</strong> ${student.email || 'Not Available'}</p>
// // //                     <p><strong>Phone Number:</strong> ${student.phone_number || 'Not Available'}</p>
// // //                     <p><strong>Department:</strong> ${student.department || 'Not Available'}</p>
// // //                     <p><strong>Course:</strong> ${student.course || 'Not Available'}</p>
// // //                     <hr>
// // //                 `;
// // //                 studentList.appendChild(studentCard);
// // //             });
// // //         })
// // //         .catch(error => console.error('Error fetching students:', error));
// // // });
// // document.addEventListener('DOMContentLoaded', () => {
// //     const studentList = document.getElementById('student-list');
// //     const searchInput = document.getElementById('searchInput');
// //     const searchCriteria = document.getElementById('searchCriteria');
// //     const searchBtn = document.getElementById('searchBtn');
// //     const clearBtn = document.getElementById('clearBtn');
// //     let studentsData = []; // Array to store all students data

// //     // Function to fetch students from API
// //     function fetchStudents() {
// //         fetch('http://demo01.com:8003/api/method/estate_app.estate_plan.api.student_api.get_students')
// //             .then(response => response.json())
// //             .then(data => {
// //                 studentsData = data.message; // Store fetched students data
// //                 displayAllStudents();
// //             })
// //             .catch(error => {
// //                 console.error('Error fetching students:', error);
// //             });
// //     }

// //     // Function to display all students
// //     function displayAllStudents() {
// //         studentList.innerHTML = ''; // Clear previous content

// //         studentsData.forEach(student => {
// //             const studentCard = createStudentCard(student);
// //             studentList.appendChild(studentCard);
// //         });
// //     }

// //     // Function to create a student card element
// //     function createStudentCard(student) {
// //         const studentCard = document.createElement('div');
// //         studentCard.classList.add('student-card');
// //         studentCard.innerHTML = `
// //             <p><strong>Register Number:</strong> ${student.register_number}</p>
// //             <p><strong>Name:</strong> ${student.name1 || 'Not Available'}</p>
// //             <p><strong>Date of Birth:</strong> ${student.date_of_birth || 'Not Available'}</p>
// //             <p><strong>Gender:</strong> ${student.gender || 'Not Available'}</p>
// //             <p><strong>Email:</strong> ${student.email || 'Not Available'}</p>
// //             <p><strong>Phone Number:</strong> ${student.phone_number || 'Not Available'}</p>
// //             <p><strong>Department:</strong> ${student.department || 'Not Available'}</p>
// //             <p><strong>Course:</strong> ${student.course || 'Not Available'}</p>
// //             <p><strong>Fees:</strong> {{ frappe.format('10000', {'fieldtype': 'Currency'}) }}</p>
// //             <hr>
// //         `;
// //         return studentCard;
// //     }

// //     // Initial fetch of students
// //     fetchStudents();

// //     // Search button click handler
// //     searchBtn.addEventListener('click', () => {
// //         const searchTerm = searchInput.value.trim().toLowerCase();
// //         const selectedCriteria = searchCriteria.value;

// //         const filteredStudents = studentsData.filter(student => {
// //             if (selectedCriteria === 'name1') {
// //                 return student.name1 && student.name1.toLowerCase().includes(searchTerm);
// //             } else if (selectedCriteria === 'register_number') {
// //                 return student.register_number.toLowerCase().includes(searchTerm);
// //             }
// //         });

// //         // Clear previous content
// //         studentList.innerHTML = '';

// //         filteredStudents.forEach(student => {
// //             const studentCard = createStudentCard(student);
// //             studentList.appendChild(studentCard);
// //         });
// //     });

// //     // Clear button click handler
// //     clearBtn.addEventListener('click', () => {
// //         searchInput.value = ''; // Clear search input
// //         displayAllStudents(); // Display all students again
// //     });
// // });
// document.addEventListener('DOMContentLoaded', () => {
//     const studentList = document.getElementById('student-list');
//     const searchInput = document.getElementById('searchInput');
//     const searchCriteria = document.getElementById('searchCriteria');
//     const searchBtn = document.getElementById('searchBtn');
//     const clearBtn = document.getElementById('clearBtn');
//     let studentsData = []; // Array to store all students data

//     // Function to fetch students from API
//     function fetchStudents() {
//         fetch('http://demo01.com:8003/api/method/estate_app.estate_plan.api.student_api.get_students')
//             .then(response => response.json())
//             .then(data => {
//                 studentsData = data.message; // Store fetched students data
//                 displayAllStudents();
//             })
//             .catch(error => {
//                 console.error('Error fetching students:', error);
//             });
//     }

//     // Function to display all students
//     function displayAllStudents() {
//         studentList.innerHTML = ''; // Clear previous content

//         studentsData.forEach(student => {
//             const studentCard = createStudentCard(student);
//             studentList.appendChild(studentCard);
//         });
//     }

//     // Function to create a student card element
//     function createStudentCard(student) {
//         const studentCard = document.createElement('div');
//         studentCard.classList.add('student-card');
//         studentCard.innerHTML = `
//             <p><strong>Register Number:</strong> ${student.register_number}</p>
//             <p><strong>Name:</strong> ${student.name1 || 'Not Available'}</p>
//             <p><strong>Date of Birth:</strong> ${formatDateOfBirth(student.date_of_birth)}</p>
//             <p><strong>Gender:</strong> ${student.gender || 'Not Available'}</p>
//             <p><strong>Email:</strong> ${student.email || 'Not Available'}</p>
//             <p><strong>Phone Number:</strong> ${student.phone_number || 'Not Available'}</p>
//             <p><strong>Department:</strong> ${student.department || 'Not Available'}</p>
//             <p><strong>Course:</strong> ${student.course || 'Not Available'}</p>
//             <hr>
//         `;
//         return studentCard;
//     }

//     // Function to format Date of Birth using Frappe's format_date
//     function formatDateOfBirth(dateOfBirth) {
//         if (!dateOfBirth) return 'Not Available';

//         // Use Frappe's format_date function
//         return `<div>${frappe.format_date(dateOfBirth)}</div>`;
//     }

//     // Initial fetch of students
//     fetchStudents();

//     // Search button click handler
//     searchBtn.addEventListener('click', () => {
//         const searchTerm = searchInput.value.trim().toLowerCase();
//         const selectedCriteria = searchCriteria.value;

//         const filteredStudents = studentsData.filter(student => {
//             if (selectedCriteria === 'name1') {
//                 return student.name1 && student.name1.toLowerCase().includes(searchTerm);
//             } else if (selectedCriteria === 'register_number') {
//                 return student.register_number.toLowerCase().includes(searchTerm);
//             }
//         });

//         // Clear previous content
//         studentList.innerHTML = '';

//         filteredStudents.forEach(student => {
//             const studentCard = createStudentCard(student);
//             studentList.appendChild(studentCard);
//         });
//     });

//     // Clear button click handler
//     clearBtn.addEventListener('click', () => {
//         searchInput.value = ''; // Clear search input
//         displayAllStudents(); // Display all students again
//     });
// });
// document.addEventListener('DOMContentLoaded', () => {
//     const studentList = document.getElementById('student-list');
//     const searchInput = document.getElementById('searchInput');
//     const searchCriteria = document.getElementById('searchCriteria');
//     const searchBtn = document.getElementById('searchBtn');
//     const clearBtn = document.getElementById('clearBtn');
//     let studentsData = []; // Array to store all students data

//     // Function to fetch students from API
//     function fetchStudents() {
//         fetch('http://demo01.com:8003/api/method/estate_app.estate_plan.api.student_api.get_students')
//             .then(response => response.json())
//             .then(data => {
//                 studentsData = data.message; // Store fetched students data
//                 displayAllStudents();
//             })
//             .catch(error => {
//                 console.error('Error fetching students:', error);
//             });
//     }

//     // Function to display all students
//     function displayAllStudents() {
//         studentList.innerHTML = ''; // Clear previous content

//         studentsData.forEach(student => {
//             const studentCard = createStudentCard(student);
//             studentList.appendChild(studentCard);
//         });
//     }

//     // Function to create a student card element
//     function createStudentCard(student) {
//         const studentCard = document.createElement('div');
//         studentCard.classList.add('student-card');
//         studentCard.innerHTML = `
//             <p><strong>Register Number:</strong> ${student.register_number}</p>
//             <p><strong>Name:</strong> ${student.name1 || 'Not Available'}</p>
//             <p><strong>Date of Birth:</strong> ${student.date_of_birth || 'Not Available'}</p>
//             <p><strong>Gender:</strong> ${student.gender || 'Not Available'}</p>
//             <p><strong>Email:</strong> ${student.email || 'Not Available'}</p>
//             <p><strong>Phone Number:</strong> ${student.phone_number || 'Not Available'}</p>
//             <p><strong>Department:</strong> ${student.department || 'Not Available'}</p>
//             <p><strong>Course:</strong> ${student.course || 'Not Available'}</p>
//             <p><strong>Fees:</strong> {{ frappe.format('10000', {'fieldtype': 'Currency'}) }}</p>
//             <hr>
//         `;
//         return studentCard;
//     }

//     // Initial fetch of students
//     fetchStudents();

//     // Search button click handler
//     searchBtn.addEventListener('click', () => {
//         const searchTerm = searchInput.value.trim().toLowerCase();
//         const selectedCriteria = searchCriteria.value;

//         const filteredStudents = studentsData.filter(student => {
//             if (selectedCriteria === 'name1') {
//                 return student.name1 && student.name1.toLowerCase().includes(searchTerm);
//             } else if (selectedCriteria === 'register_number') {
//                 return student.register_number.toLowerCase().includes(searchTerm);
//             }
//         });

//         // Clear previous content
//         studentList.innerHTML = '';

//         filteredStudents.forEach(student => {
//             const studentCard = createStudentCard(student);
//             studentList.appendChild(studentCard);
//         });
//     });

//     // Clear button click handler
//     clearBtn.addEventListener('click', () => {
//         searchInput.value = ''; // Clear search input
//         displayAllStudents(); // Display all students again
//     });
// });
document.addEventListener('DOMContentLoaded', () => {
    const studentList = document.getElementById('student-list');
    const searchInput = document.getElementById('searchInput');
    const searchCriteria = document.getElementById('searchCriteria');
    const searchBtn = document.getElementById('searchBtn');
    const clearBtn = document.getElementById('clearBtn');
    const paginationContainer = document.getElementById('paginationContainer');
    
    let studentsData = []; // Array to store all students data
    let currentPage = 1; // Current page of pagination
    const recordsPerPage = 5; // Number of records per page

    // Function to fetch students from API
    function fetchStudents() {
        fetch('http://demo01.com:8003/api/method/estate_app.estate_plan.api.student_api.get_students')
            .then(response => response.json())
            .then(data => {
                studentsData = data.message; // Store fetched students data
                displayAllStudents();
            })
            .catch(error => {
                console.error('Error fetching students:', error);
            });
    }

    // Function to display students based on current page
    function displayAllStudents() {
        studentList.innerHTML = ''; // Clear previous content

        const startIndex = (currentPage - 1) * recordsPerPage;
        const endIndex = startIndex + recordsPerPage;
        const currentStudents = studentsData.slice(startIndex, endIndex);

        currentStudents.forEach(student => {
            const studentCard = createStudentCard(student);
            studentList.appendChild(studentCard);
        });

        renderPagination(); // Render pagination controls
    }

    // Function to create a student card element
    function createStudentCard(student) {
        const studentCard = document.createElement('div');
        studentCard.classList.add('student-card');
        studentCard.innerHTML = `
            <p><strong>Register Number:</strong> ${student.register_number}</p>
            <p><strong>Name:</strong> ${student.name1 || 'Not Available'}</p>
            <p><strong>Date of Birth:</strong> ${student.date_of_birth || 'Not Available'}</p>
            <p><strong>Gender:</strong> ${student.gender || 'Not Available'}</p>
            <p><strong>Email:</strong> ${student.email || 'Not Available'}</p>
            <p><strong>Phone Number:</strong> ${student.phone_number || 'Not Available'}</p>
            <p><strong>Department:</strong> ${student.department || 'Not Available'}</p>
            <p><strong>Course:</strong> ${student.course || 'Not Available'}</p>
            <p><strong>Fees:</strong> {{ frappe.format('10000', {'fieldtype': 'Currency'}) }}</p>
            <hr>
        `;
        return studentCard;
    }

    // Function to render pagination controls
    function renderPagination() {
        const totalPages = Math.ceil(studentsData.length / recordsPerPage);

        // Clear previous pagination controls
        paginationContainer.innerHTML = '';

        // Create previous button
        const prevBtn = document.createElement('button');
        prevBtn.textContent = 'Previous';
        prevBtn.disabled = currentPage === 1;
        prevBtn.addEventListener('click', () => {
            if (currentPage > 1) {
                currentPage--;
                displayAllStudents();
            }
        });
        paginationContainer.appendChild(prevBtn);

        // Create next button
        const nextBtn = document.createElement('button');
        nextBtn.textContent = 'Next';
        nextBtn.disabled = currentPage === totalPages;
        nextBtn.addEventListener('click', () => {
            if (currentPage < totalPages) {
                currentPage++;
                displayAllStudents();
            }
        });
        paginationContainer.appendChild(nextBtn);
    }

    // Initial fetch of students and display
    fetchStudents();

    // Search button click handler
    searchBtn.addEventListener('click', () => {
        currentPage = 1; // Reset to first page on search
        const searchTerm = searchInput.value.trim().toLowerCase();
        const selectedCriteria = searchCriteria.value;

        const filteredStudents = studentsData.filter(student => {
            if (selectedCriteria === 'name1') {
                return student.name1 && student.name1.toLowerCase().includes(searchTerm);
            } else if (selectedCriteria === 'register_number') {
                return student.register_number.toLowerCase().includes(searchTerm);
            }
        });

        // Update displayed students and pagination
        studentList.innerHTML = '';
        filteredStudents.forEach(student => {
            const studentCard = createStudentCard(student);
            studentList.appendChild(studentCard);
        });
        renderPagination(); // Render pagination controls
    });

    // Clear button click handler
    clearBtn.addEventListener('click', () => {
        searchInput.value = ''; // Clear search input
        currentPage = 1; // Reset to first page on clear
        displayAllStudents(); // Display all students again
    });
});
