let inputBox = $("#newTodo");
let addBtn = $("#addTodo");
let todoList = $("#todoList");
let deleteAllBtn = $("#deleteAllTodo");

inputBox.on("input", function (){
    if ($(inputBox).val().length > 0) {
        addBtn.addClass("active")
    }
    else{
        addBtn.removeClass("active")
    }
})

showTasks();



function showTasks(entries){
    const pendingTasksNumb = $(".pendingTasks");
    pendingTasksNumb.text(entries.length)

    if(entries.length > 0){
        deleteAllBtn.addClass("active");
    }else{
        deleteAllBtn.removeClass("active");
    }
    let newLiTag = "";
    entries.forEach((element, index) => {
        newLiTag += `<li>${element}<span class="icon" onclick="deleteTask(${index})"><i class="fas fa-trash"></i></span></li>`;
    });

    todoList.html(newLiTag);
    inputBox.value = "";
}
function deleteTask(index){
    $.ajax({
        type: "POST",
        url: "/todo",
        data: {index:index},
        success:function (){
            notify('Successfully deleted!', 'success')
            location.reload()
        }
    })

    let getLocalStorageData = localStorage.getItem("New Todo");
    listArray = JSON.parse(getLocalStorageData);
    listArray.splice(index, 1);
    localStorage.setItem("New Todo", JSON.stringify(listArray));
    showTasks();
}
deleteAllBtn.onclick = ()=>{
    listArray = [];
    localStorage.setItem("New Todo", JSON.stringify(listArray));
    showTasks();
}
