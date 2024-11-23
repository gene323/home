import * as ghpages from 'gh-pages';
import * as fs from "fs";

fs.writeFile('./dist/CNAME', 'meowju.me', (err) => {
	if (err) {
		console.log(err)
	}
	else {
		console.log('write CNAME FILE DONE.')

		// deploy to github
		ghpages.publish('dist', {
			branch: 'main',
			repo: 'git@github.com:gene323/home.git',
			message: 'Auto-generated commit',
		})
	}
})
