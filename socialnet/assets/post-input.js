var accordions = document.getElementsByClassName("collapsible-toggle");

for(var i=0;i<accordions.length;i++){
  accordions[i].onclick=function(){
    this.classList.toggle("active");
    this.nextElementSibling.classList.toggle("show");
  }
}
