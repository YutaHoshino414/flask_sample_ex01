
const Hello = {
    data() {
        return {
            message: 'API from Vue.js',
            results:[]
        }
    },
    delimiters: ['{', '}'],
    created(){
        fetch("https://www.omdbapi.com/?s=man&apikey=")
        .then(response =>  response.json())
        .then( data =>{ 
            console.log(data["Search"]);
            this.results = data["Search"]
        })
    }
    
}

const Task = {
    data() {
        return {
            task: 'New Task',
            results: []
        }
    },
    delimiters: ['{', '}'],
    mounted() {
    axios.get("http://zipcloud.ibsnet.co.jp/api/search?zipcode=1910032")
    .then(response => {this.results = response.data.results})
    }
};

Vue.createApp(Hello).mount('#app')
Vue.createApp(Task).mount('#task')
