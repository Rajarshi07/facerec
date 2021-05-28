async function forcehttps(){
    const hostname = await window.location.hostname;
    console.log(hostname);
    localhost = ['localhost','127.0.0.1']
    if(hostname==localhost[1] || hostname==localhost[0])return false;
    else if(location.protocol !== 'https:') {
        console.log("forcing https")
        location.replace(`https:${location.href.substring(location.protocol.length)}`);
    }
}
forcehttps()