const hello = 'Hello World!';


for(let i=0; i < hello.length ; i++){
    if(hello[i] === ' '){
        console.log('----------');
    }
    else{
        console.log('| \t |', hello[i]);
    }
}