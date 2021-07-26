from UI_shizhan.page.base_page import BasePage


class Search(BasePage):
    def search(self, name):
        self._params['name'] = name
        self.steps('../page/search.yaml')
        # with open('../page/search.yaml', encoding='utf-8') as f:
        #     steps = yaml.safe_load(f)
        # for step in steps:
        #     element = None
        #     if 'by' in step.keys():
        #         element = self.find(step['by'], step['locator'])
        #     if 'action' in step.keys():
        #         action = step['action']
        #         if 'click' == action:
        #             element.click()
        #         if 'send' == action:
        #             element.send_keys(step['value'])

    def add(self, name):
        self._params['name'] = name
        self.steps('../page/search.yaml')

    def is_choose(self, name):
        self._params['name'] = name
        return self.steps('../page/search.yaml')

    def reset(self, name):
        self._params['name'] = name
        return self.steps('../page/search.yaml')
