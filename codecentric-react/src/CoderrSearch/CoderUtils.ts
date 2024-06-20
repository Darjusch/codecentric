import axios from "axios";
const token = process.env.REACT_APP_GITHUB_TOKEN;

const axiosInstance = axios.create({
  headers: {
    Authorization: `token ${token}`,
  },
});

export const getMembers = async () => {
  const response = await axiosInstance.get(
    "https://api.github.com/orgs/codecentric/members"
  );
  return response.data;
};

export const getRepos = async (member: string) => {
  const response = await axiosInstance.get(
    `https://api.github.com/users/${member}/repos`
  );
  return response.data;
};

export const getLanguages = async (member: string, repo: string) => {
  const response = await axiosInstance.get(
    `https://api.github.com/repos/${member}/${repo}/languages`
  );
  return response.data;
};

export const getMembersRepos = async () => {
  const members = await getMembers();
  const repos = await Promise.all(
    members.map(async (member: any) => {
      const memberRepos = await getRepos(member.login);
      return memberRepos;
    })
  );
  return repos;
};

export const findFirstCoderByLanguageInRepos = async (language: string) => {
  const repose = await getMembersRepos();
  for (const memberRepos of repose) {
    for (const repo of memberRepos) {
      const languages = await getLanguages(repo.owner.login, repo.name);
      if (languages[language]) {
        return repo.owner.login;
      }
    }
  }
  return null;
};
