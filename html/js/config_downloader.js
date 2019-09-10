


function download_config_file(host,port,user,pass,pub_topic,sub_topic)
{

sessionStorage.setItem("mqhost",host)
sessionStorage.setItem("mqport",port)
sessionStorage.setItem("mquser",user)
sessionStorage.setItem("mqpass",pass)
sessionStorage.setItem("mqpubtopic",pub_topic)
sessionStorage.setItem("mqsubtopic",sub_topic)

// then redirect the page using window.location.href="download.html"
window.location.href = "download.html"
}
