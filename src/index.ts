
const districts = require('../data/minified/districts.min.json');
const stateanimals = require('../data/minified/stateanimals.min.json');
const statebirds = require('../data/minified/statebirds.min.json');
const stateflowers = require('../data/minified/stateflowers.min.json');
const statetrees = require('../data/minified/statetrees.min.json');

const dataForIndia = {
	districts: districts.districts,
	stateAnimals: stateanimals.stateAnimals,
	stateBirds: statebirds.stateBirds,
	stateFlowers: stateflowers.stateFlowers,
	stateTrees: statetrees.stateTrees,
};

module.exports = dataForIndia;
