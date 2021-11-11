const Hello = {
    data() {
        return {
            message: 'Hello world from Vue.js'
        }
    },
    delimiters: ['{', '}']
}

const Task = {
    data() {
        return {
            task: 'New Task',

            tasks: [
                {title:'one'},
                {title:'two'},
                {title:'three'},
            ]
        }
    },
    delimiters: ['{', '}']
}

Vue.createApp(Hello).mount('#app')
Vue.createApp(Task).mount('#task')