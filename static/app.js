const NATIONS = "СССР, США, Германия, Великобритания, Китай, Италия, Чехословакия, Япония, Польша, Франция, Швеция"
const TYPES = "САУ, ПТ САУ, Легкий танк, Тяжелый танк, Средний танк"
const TIERS = "10, 9, 8"

new Vue({
    el: '#tanks-base',
    data: {
    tanks: [],
    keyword: '',
    nations: NATIONS.split(', '), // create an array of the nations
    nation: '', // set default nation to ''
    types: TYPES.split(', '), // create an array of the types
    type: '', // set default  to ''
    tiers: TIERS.split(', '), // create an array of the tiers
    tier: '', // set default  to ''
    loading: true,
    },

    methods: {
    getBase() {
        axios.get('/api/tanksbase/')
        .then(response => (this.tanks = response.data))
        .catch(err => console.log(err));
        },

    getSearchName(keyword) {
        axios.get('/api/tanksbase/?search='+this.keyword.toUpperCase())
        .then(response => (this.tanks = response.data))

        },
    clearSearch() {
        this.keyword = '';
        axios.get('/api/tanksbase/')
        .then(response => (this.tanks = response.data))
        .catch(err => console.log(err));
        },
    resetFilters() {
        this.nation = '';
        this.type = '';
        this.tier = '';
        axios.get('/api/tanksbase/')
        .then(response => (this.tanks = response.data))
        .catch(err => console.log(err));
    },



    getFiltered(nation, type, tier) {
      axios.get('/api/tanksbase/?nation='+this.nation+'&type='+this.type+'&tier='+this.tier)
      .then((response) => {
        this.loading = false;
        this.tanks = response.data;
      })
       .catch(err => console.log(err));
        },
    },

    mounted() {
     this.getBase ();
      },

    computed: {
    searchName() {
        console.log('Searching name')
        return this.getSearchName(keyword)
    },
    filtered() {
        return this.getFiltered(nation, type, tier)
    },
    },
}
)

