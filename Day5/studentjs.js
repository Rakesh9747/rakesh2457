
var selectedRow = null;
function onFormSubmit() {
var formData = readFormData();
if(isValid()){
    if (selectedRow == null) {
    insertNewRecord(formData);
    alert("Your details are saved Sucessfully........");
  }
 else{
  updateRecord(formData);
 }
  resetForm();
}
}

function readFormData() {
  var formData = {};
  formData["stuName"] = document.getElementById("stuName").value;
  formData["stucollege"] = document.getElementById("stucollege").value;
  formData["stucou"] = document.getElementById("stucou").value;
  return formData;
}
function resetForm() {
  document.getElementById("stuName").value = "";
  document.getElementById("stucollege").value = "";
  document.getElementById("stucou").value = "";
 
  selectedRow = null;
}
function insertNewRecord(data) {
  var table = document
    .getElementById("studentlist")
    .getElementsByTagName("tbody")[0];
  var newRow = table.insertRow(table.length);
  cell1 = newRow.insertCell(0);
  cell1.innerHTML = data.stuName;
  cell2 = newRow.insertCell(1);
  cell2.innerHTML = data.stucollege;
  cell3 = newRow.insertCell(2);
  cell3.innerHTML = data.stucou;
  cell4 = newRow.insertCell(3);
  cell4.innerHTML = `<a onClick="onEdit(this)">Update</a><a onClick="onDelete(this)">Delete</a>`;
}
function onEdit(td)
{if(confirm("Are you upadate your details")){
selectedRow=td.parentElement.parentElement;  
document.getElementById("stuName").value=selectedRow.cells[0].innerHTML;
document.getElementById("stucollege").value=selectedRow.cells[1].innerHTML;
document.getElementById("stucou").value=selectedRow.cells[2].innerHTML;
}
}
function updateRecord(formData)
{
  alert("Your form updated sucessfully.......")
selectedRow.cells[0].innerHTML=formData.stuName;
selectedRow.cells[1].innerHTML=formData.stucollege;
selectedRow.cells[2].innerHTML=formData.stucou;

}
function onDelete(td)
{
if(confirm("are you want to delete this record")){
  row=td.parentElement.parentElement;
  document.getElementById("studentlist").deleteRow(row.rowIndex);
  resetForm();
}
}

function isValid(){
var a=document.getElementById("stuName").value;
// var  b = document.getElementById("facDep").value;
// var c= document.getElementById("facSub").value;
// var d= document.getElementById("facAge").value;
//  var e= document.getElementById("facPlace").value;
if(a==""|| a==null ){return false;}
else
{return true;}

}

 