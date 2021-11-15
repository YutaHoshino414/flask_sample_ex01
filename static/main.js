
const Hello = {
    data() {
        return {
            message: 'Hello world from Vue.js',
            results:[]
        }
    },
    delimiters: ['{', '}'],
    mounted(){
        fetch("https://www.omdbapi.com/?s=man&apikey=4a3b711b")
        .then(response => {return response.json();
        })
        .then( response =>{ 
            console.log(response.Search);
            this.results = response.Search
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
