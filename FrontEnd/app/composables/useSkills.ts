export interface SkillLevel {
  skill: string
  level: number
  category?: string
}

export const useSkills = () => {
  const authStore = useAuthStore()
  const api = useApi()

  const userSkills = computed(() => authStore.user?.skills || [])

  const skillCategories = [
    { value: 'programming', label: 'Programming & Development' },
    { value: 'design', label: 'Design & Creative' },
    { value: 'data-science', label: 'Data Science & Analytics' },
    { value: 'marketing', label: 'Marketing & Communication' },
    { value: 'business', label: 'Business & Management' },
    { value: 'soft-skills', label: 'Soft Skills' }
  ]

  const addSkill = async (skill: string) => {
    if (!skill || !skill.trim()) {
      throw new Error('Skill cannot be empty')
    }

    try {
      const updatedUser = await authStore.addSkill(skill.trim())
      return updatedUser
    } catch (err) {
      throw err
    }
  }

  const removeSkill = async (skill: string) => {
    try {
      const updatedUser = await authStore.removeSkill(skill)
      return updatedUser
    } catch (err) {
      throw err
    }
  }

  const updateSkills = async (skills: string[]) => {
    try {
      const updatedUser = await authStore.updateProfile({ skills })
      return updatedUser
    } catch (err) {
      throw err
    }
  }

  const categorizeSkills = (skills: string[]): Record<string, string[]> => {
    const categorized: Record<string, string[]> = {
      'programming': [],
      'design': [],
      'data-science': [],
      'marketing': [],
      'business': [],
      'soft-skills': [],
      'other': []
    }

    const programmingKeywords = ['javascript', 'python', 'java', 'react', 'vue', 'node', 'typescript', 'html', 'css', 'sql', 'git', 'docker', 'kubernetes', 'aws', 'api', 'backend', 'frontend', 'fullstack', 'web development', 'mobile development']
    const designKeywords = ['figma', 'sketch', 'adobe', 'photoshop', 'illustrator', 'ui', 'ux', 'design', 'wireframe', 'prototype', 'visual design']
    const dataScienceKeywords = ['data', 'analytics', 'machine learning', 'ai', 'python', 'r', 'tableau', 'power bi', 'sql', 'statistics', 'modeling']
    const marketingKeywords = ['marketing', 'seo', 'social media', 'content', 'copywriting', 'email', 'advertising', 'google analytics', 'campaigns']
    const businessKeywords = ['management', 'project', 'agile', 'scrum', 'leadership', 'strategy', 'business', 'planning', 'sales']
    const softSkillsKeywords = ['communication', 'teamwork', 'problem solving', 'critical thinking', 'time management', 'adaptability', 'creativity', 'collaboration']

    skills.forEach(skill => {
      const lowerSkill = skill.toLowerCase()
      let categorized_flag = false

      if (programmingKeywords.some(kw => lowerSkill.includes(kw))) {
        categorized['programming']?.push(skill)
        categorized_flag = true
      }
      if (designKeywords.some(kw => lowerSkill.includes(kw))) {
        categorized['design']?.push(skill)
        categorized_flag = true
      }
      if (dataScienceKeywords.some(kw => lowerSkill.includes(kw))) {
        categorized['data-science']?.push(skill)
        categorized_flag = true
      }
      if (marketingKeywords.some(kw => lowerSkill.includes(kw))) {
        categorized['marketing']?.push(skill)
        categorized_flag = true
      }
      if (businessKeywords.some(kw => lowerSkill.includes(kw))) {
        categorized['business']?.push(skill)
        categorized_flag = true
      }
      if (softSkillsKeywords.some(kw => lowerSkill.includes(kw))) {
        categorized['soft-skills']?.push(skill)
        categorized_flag = true
      }
      
      if (!categorized_flag) {
        categorized['other']?.push(skill)
      }
    })

    return categorized
  }

  const getSkillSuggestions = (input: string): string[] => {
    const commonSkills = [
      'JavaScript', 'Python', 'React', 'Vue.js', 'Node.js', 'TypeScript',
      'HTML/CSS', 'SQL', 'Git', 'Docker', 'AWS', 'RESTful APIs',
      'Figma', 'Adobe XD', 'UI/UX Design', 'Photoshop',
      'Data Analysis', 'Excel', 'Tableau', 'Power BI',
      'SEO', 'Social Media Marketing', 'Content Writing',
      'Project Management', 'Agile', 'Scrum',
      'Communication', 'Teamwork', 'Problem Solving', 'Leadership'
    ]

    if (!input || input.length < 2) return []

    return commonSkills.filter(skill =>
      skill.toLowerCase().includes(input.toLowerCase())
    ).slice(0, 10)
  }

  return {
    userSkills,
    skillCategories,
    addSkill,
    removeSkill,
    updateSkills,
    categorizeSkills,
    getSkillSuggestions
  }
}

